
"""
Imports
"""
# imports for GUI
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# imports for search
import json
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
import os.path
import os
from whoosh.qparser import QueryParser

"""
Global variables
"""
Hitted_ids = list()
Hitted_recipe_names = list()

"""
Functions
"""
# parse query and when the user types and stores matches in hitted ids and recipe names, then updates table model
def actOnType():
    user_query = searchField.text()
    qp = QueryParser("name", schema=ix.schema)
    q = qp.parse(user_query)
    with ix.searcher() as searcher:
        results = searcher.search(q, limit=10)
        Store_Matches(results)
    print("input is: " + user_query)
    print(Hitted_recipe_names)

    model = getTableModel()
    recipeList.setModel(model)
    recipeList.setColumnWidth(1, 500)

# Store the search results, id and recipe name into two list
def Store_Matches(results):
    global Hitted_ids
    global Hitted_recipe_names
    # Refresh
    Hitted_ids = list()
    Hitted_recipe_names = list()

    for hit in results:
        Hitted_ids.append(hit['id'])
        Hitted_recipe_names.append(hit["name"])

# Create table model from recipe id and recipe name global variables
def getTableModel():
    global Hitted_ids
    global Hitted_recipe_names

    model = QStandardItemModel(len(Hitted_recipe_names),2)

    for row, id in enumerate(Hitted_ids):
        item = QStandardItem(id)
        model.setItem(row,0,item)

    for row, name in enumerate(Hitted_recipe_names):
        item = QStandardItem(name)
        model.setItem(row,1,item)

    return model

schema = Schema(
    name=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    id=ID(stored=True)
)

"""
Main program
"""


"""
Set up index for search
"""

# create an index object
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = index.create_in("indexdir", schema)

# get index writer object
writer = ix.writer()

# open json, loop through list and add each recipe object as a document to the index
x = open('partial_layer1.json')
layer1 = json.load(x)
for i in range(0, len(layer1)):
    writer.add_document(name=layer1[i]["title"], id=layer1[i]["id"])
writer.commit()


"""
Set up GUI
"""
app = QApplication(sys.argv)

# Set up window and overall layout
window = QWidget()
window.setWindowTitle('Foodkg Search Tool')
window.setGeometry(500, 300, 500, 200)

layout = QGridLayout()
layout.setColumnStretch(0, 5)

# Set up search box
searchField = QLineEdit()
searchField.textChanged.connect(actOnType)
layout.addWidget(searchField, 0, 0)

# Set up table
recipeList = QTableView()
recipeList.verticalHeader().setVisible(False)
recipeList.horizontalHeader().setVisible(False)
layout.addWidget(recipeList, 1, 0)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())



