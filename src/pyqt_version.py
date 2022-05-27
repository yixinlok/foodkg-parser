""""Simple Hello World example with PyQt5."""

import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableView


def greeting():
    recipeList.setText("Hello World!")

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('Foodkg Search Tool')
window.setGeometry(500, 300, 500, 200)

layout = QGridLayout()
layout.setColumnStretch(0,5)
searchField = QLineEdit('Enter recipe here')
searchField.textChanged.connect(greeting)
layout.addWidget(searchField,0,0)

# searchButton = QPushButton('Search')
# searchButton.clicked.connect(greeting)
# layout.addWidget(searchButton,0,1)

recipeList = QLabel("recipe list")
layout.addWidget(recipeList,1,0)

window.setLayout(layout)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())

