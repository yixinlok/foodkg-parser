

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

from gui_functions import *

'''
Main program
'''
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
