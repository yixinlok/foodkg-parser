
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# data
Hitted_recipe_id = ['000018c8a5', '0001d356b6']
Hitted_recipe_names = ['Worlds Best Mac and Cheese',
                       'Lemon Cupcakes with Blueberry Compote Filling and Cream Cheese Frosting']
Hitted_ingredients = ['Cheese, Macaroni, Sugar',
                      'Blueberry compote, cream cheese, flour']
Hitted_nutri = [
    {
        "protein": "1000",
        "fat": "1000"
    },
    {
        "protein": "200",
        "fat": "2000"
    }
]


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
    user_query = nameSearchField.text()
    print("name search input is: " + user_query)


def actOnIngrType():
    user_query = ingrSearchField.text()
    print("ingr search input is: " + user_query)


def createNameSearchBar():
    layout.addWidget(QLabel("name search: "), 0, 0)
    nameSearchField = QLineEdit()
    nameSearchField.textChanged.connect(actOnNameType)
    layout.addWidget(nameSearchField, 0, 1, 1, 3)


def createIngredientSearchBar():
    layout.addWidget(QLabel("ingredient search: "), 1, 0)
    ingrSearchField = QLineEdit()
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
    model = getTableModel(Hitted_recipe_id, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList = QTableView()
    recipeList.setModel(model)
    recipeList.verticalHeader().setVisible(False)
    recipeList.setColumnWidth(1, 500)
    recipeList.resizeColumnsToContents()
    layout.addWidget(recipeList, 3, 0, 1, 4)


# Main program
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Foodkg Search Tool')
window.setGeometry(400, 250, 800, 300)
layout = QGridLayout()

createNameSearchBar()
createIngredientSearchBar()
createCheckBoxes()
createTable()

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
