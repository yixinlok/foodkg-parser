
import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

def getTableModel(Hitted_recipe_id, Hitted_recipe_names):
    model = QStandardItemModel(len(Hitted_recipe_names),2)

    for row, id in enumerate(Hitted_recipe_id):
        item = QStandardItem(id)
        model.setItem(row,0,item)

    for row, name in enumerate(Hitted_recipe_names):
        item = QStandardItem(name)
        model.setItem(row,1,item)

    return model

def actOnType():
    user_query = searchField.text()
    print("input is: " + user_query)

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('Foodkg Search Tool')
window.setGeometry(500, 300, 500, 200)

layout = QGridLayout()
layout.setColumnStretch(0, 5)
searchField = QLineEdit()
searchField.textChanged.connect(actOnType)
layout.addWidget(searchField, 0, 0)

Hitted_recipe_id = ['000018c8a5', '0001d356b6']
Hitted_recipe_names = ['Worlds Best Mac and Cheese', 'Lemon Cupcakes with Blueberry Compote Filling and Cream Cheese Frosting']

model = getTableModel(Hitted_recipe_id, Hitted_recipe_names)
recipeList = QTableView()
recipeList.setModel(model)
recipeList.verticalHeader().setVisible(False)
recipeList.horizontalHeader().setVisible(False)
recipeList.setColumnWidth(1, 500)
layout.addWidget(recipeList, 1, 0)

window.setLayout(layout)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())
