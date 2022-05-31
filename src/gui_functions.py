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
    name_query = nameSearchField.text()
    print("name search input is: " + name_query)
    actOnState()
    createTable()


def actOnIngrType():
    ingr_query = ingrSearchField.text()
    print("ingr search input is: " + ingr_query)
    actOnState()
    createTable()


def actOnState():
    qp = QueryParser("name", schema=ix.schema)
    q = qp.parse(name_query)
    allow_q = query.Term("ingredients", ingr_query)

    with ix.searcher() as searcher:
        results = s.search(q, filter=allow_q, limit=10)
        Store_Matches(results)
    return


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
    recipeList = QTableView()
    recipeList.verticalHeader().setVisible(False)
    recipeList.setColumnWidth(1, 500)
    recipeList.resizeColumnsToContents()
    model = getTableModel(Hitted_recipe_id, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList.setModel(model)
    layout.addWidget(recipeList, 3, 0, 1, 4)
