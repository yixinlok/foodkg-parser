'''
Imports
'''
import sys

import json
from whoosh import index, query
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
import os.path
import os
from whoosh.qparser import QueryParser, OrGroup

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem

'''
Globals
'''
name_query = ""
ingr_query = ""

Hitted_ids = list()
Hitted_recipe_names = list()
Hitted_ingredients = list()
Hitted_nutri = list()

'''
Functions
'''


def Store_Matches(results):
    global Hitted_ids
    global Hitted_recipe_names
    global Hitted_ingredients
    global Hitted_nutri

    # Refresh
    Hitted_ids = list()
    Hitted_recipe_names = list()
    Hitted_ingredients = list()
    Hitted_nutri = list()

    print(results)
    # Store the results
    for hit in results:
        Hitted_ids.append(hit['id'])
        Hitted_recipe_names.append(hit["name"])
        Hitted_ingredients.append(hit["ingredients"])
        Hitted_nutri.append(hit["nutri_info"])


def getTableModel(Hitted_recipe_id, Hitted_recipe_names, Hitted_ingredients, Hitted_nutri):
    model = QStandardItemModel(len(Hitted_recipe_names), 2)

    for row, id in enumerate(Hitted_recipe_id):
        item = QStandardItem(id)
        model.setItem(row, 0, item)

    for row, name in enumerate(Hitted_recipe_names):
        item = QStandardItem(name)
        model.setItem(row, 1, item)

    for row, ingr in enumerate(Hitted_ingredients):
        item = QStandardItem(ingr)
        model.setItem(row, 2, item)

    for row, nutri in enumerate(Hitted_nutri):
        item = QStandardItem(str(nutri))
        model.setItem(row, 3, item)

    model.setHorizontalHeaderLabels(
        ['ID', 'Recipe Name', 'Ingredients', 'Nutritional Information'])

    return model


def actOnNameType():
    global name_query
    global nameSearchField
    global recipeList

    name_query = nameSearchField.text()
    print("name search input is: " + name_query)
    actOnState()
    model = getTableModel(Hitted_ids, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList.setModel(model)
    recipeList.resizeColumnsToContents()


def actOnIngrType():
    global ingrSearchField
    global ingr_query
    global recipeList

    ingr_query = ingrSearchField.text()
    print("ingr search input is: " + ingr_query)
    actOnState()
    model = getTableModel(Hitted_ids, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList.setModel(model)
    recipeList.resizeColumnsToContents()


def actOnState():
    global name_query
    global ingr_query

    if name_query!="" and ingr_query!="":
        qp = QueryParser("name", schema=ix.schema)
        q = qp.parse(name_query)
        if ingr_query[0] == "!":
            not_allow = query.Term("ingredients", ingr_query[1:len(ingr_query)])
            with ix.searcher() as searcher:
                results = searcher.search(q, mask=not_allow, limit=10)
                Store_Matches(results)
        else:
            allow_q = query.Term("ingredients", ingr_query)

            with ix.searcher() as searcher:
                results = searcher.search(q, filter=allow_q, limit=10)
                Store_Matches(results)

    elif name_query=="" and ingr_query!="":
        qp = QueryParser("ingredients", schema=ix.schema)
        q = qp.parse(ingr_query)

        with ix.searcher() as searcher:
            results = searcher.search(q, limit=10)
            Store_Matches(results)
    else:
        qp = QueryParser("name", schema=ix.schema)
        q = qp.parse(name_query)

        with ix.searcher() as searcher:
            results = searcher.search(q, limit=10)
            Store_Matches(results)


def createNameSearchBar():
    global nameSearchField
    layout.addWidget(QLabel("name search: "), 0, 0)
    nameSearchField.textChanged.connect(actOnNameType)
    layout.addWidget(nameSearchField, 0, 1, 1, 3)


def createIngredientSearchBar():
    global ingrSearchField
    layout.addWidget(QLabel("ingredient search: "), 1, 0)
    ingrSearchField.textChanged.connect(actOnIngrType)
    layout.addWidget(ingrSearchField, 1, 1, 1, 3)


def createCheckBoxes():
    fatCheckBox = QCheckBox('Low fat')
    layout.addWidget(fatCheckBox, 2, 0, 1, 1)
    saltCheckBox = QCheckBox('Low salt')
    layout.addWidget(saltCheckBox, 2, 1, 1, 1)
    saturatesCheckBox = QCheckBox('Low saturates')
    layout.addWidget(saturatesCheckBox, 2, 2, 1, 1)
    sugarCheckBox = QCheckBox('Low sugar')
    layout.addWidget(sugarCheckBox, 2, 3, 1, 1)


def createTable():
    recipeList.verticalHeader().setVisible(False)
    model = getTableModel(Hitted_ids, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList.setModel(model)
    recipeList.resizeColumnsToContents()
    layout.addWidget(recipeList, 3, 0, 1, 4)


'''
Main program
'''

''' set up search '''
schema = Schema(
    name=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    id=ID(stored=True),
    ingredients=KEYWORD(stored=True, commas=True, analyzer=StemmingAnalyzer()),
    nutri_info=TEXT(stored=True)
)

# create an index object
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = index.create_in("indexdir", schema)

# addDocsToIndex()
writer = ix.writer()
x = open('/Users/maxwang/Desktop/json/recipes_with_nutritional_info.json')
layer1 = json.load(x)
for i in range(0, len(layer1)):
    ingredients1 = ""
    for j in range(0, len(layer1[i]["ingredients"])):
        ingredients1 += layer1[i]["ingredients"][j]["text"]
    writer.add_document(name=layer1[i]["title"], id=layer1[i]["id"], ingredients=ingredients1,
                        nutri_info=str(layer1[i]["nutr_values_per100g"]))

writer.commit()

''' set up GUI '''
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Foodkg Search Tool')
window.setGeometry(400, 250, 800, 300)
layout = QGridLayout()

nameSearchField = QLineEdit()
ingrSearchField = QLineEdit()
recipeList = QTableView()

createNameSearchBar()
createIngredientSearchBar()
# createCheckBoxes()
createTable()

# send to GUI and exit
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
