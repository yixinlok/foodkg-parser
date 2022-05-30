
import json
from whoosh import index, query
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
import os.path
import os
from whoosh.qparser import QueryParser, OrGroup




# Global variable
Hitted_ids = list()
Hitted_recipe_names = list()

#Print Menu
#print("---------------------")


# Store the results, id and recipe name into two list
def Store_Matches():
    global Hitted_ids
    global Hitted_recipe_names
    global Hitted_nutri
    # Refresh
    Hitted_ids = list()
    Hitted_recipe_names = list()
    Hitted_nutri = list()
    for hit in results:
        Hitted_ids.append(hit['id'])
        Hitted_recipe_names.append(hit["name"])
        Hitted_nutri.append(hit["nutri_info"])

def print_result(results):
    # print the mactched recipe id and the name of the recipes (range(len(results)))
    print("----------------------------------")
    print("Matched results,\n#.(Recipe name, id, nutritional data)")

    for hit in range(0, len(Hitted_recipe_names)):
        print(str(hit+1) + "." +
            "(" + Hitted_recipe_names[hit] + ", " + Hitted_ids[hit] + ", " + Hitted_nutri[hit] + ")")

    # print the stats
    # Note: The Results object acts like a list of the matched documents. You can use it to access the stored fields of each hit document, to display to the user.
    print("----------------------------------")
    print("The stats")
    print("number of results:", len(results))
    print("Searching stats:", results)

# def search_ingredients():
# while(True):
#     answer = input("Do you want to search by ingredients? (y = yes, n = no)")
#     if answer == "y" or "Y":
#         queryParser("ingredients",ix.schema)
#         user_query("Type in the sepcific ingredient, if more than one use ',' to separte")
#         break
#     elif answer == "n" or "N":
#         break
#     else:
#         print("Wrong answer")








# schema = Schema(
#     ingredients=TEXT(stored=True),
#     url=ID(stored=True),
#     partition=TEXT(stored=True),
#     title=TEXT(stored=True),
#     id=ID(stored=True),
#     instructions=TEXT(stored=True)
# )
# set up schema
    ''' Note: If you aren’t specifying any constructor keyword arguments to one of the predefined fields,
    you can leave off the brackets (e.g. fieldname=TEXT instead of fieldname=TEXT()).
    Whoosh will instantiate the class for you.'''
schema = Schema(
    name=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    id=ID(stored=True),
    ingredients=KEYWORD(stored=True,commas=True),
    nutri_info = TEXT(stored = True)
)

# create an index object
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
# get index writer object
writer = ix.writer()

# open json, loop through list and add each recipe object as a document to the index
x = open('recipes_with_nutritional_info.json')
layer1 = json.load(x)
for i in range(0, len(layer1)):
    ingredients1 = ""
    for j in range(0,len(layer1[i]["ingredients"])):
        ingredients1 += layer1[i]["ingredients"][j]["text"]
    writer.add_document(name=layer1[i]["title"], id=layer1[i]["id"],ingredients = ingredients1,
    nutri_info = str(layer1[i]["nutr_values_per100g"]))

writer.commit()

#Infinite loop to avoid reading json repetitively 
open = True



while(open):
    ingredients_search = True
    # takes in name of the default field to search, and the name of the schema
    qp = QueryParser("name", schema=ix.schema)
    print("Type 0 if you want to stop the search.")
    user_query = input("Search recipe: ")
    if user_query == '0':
        print("Thank you for using the search tool")
        break

    q = qp.parse(user_query)
    # index searcher object
    with ix.searcher() as searcher:

        while(True):
            answer = input("Do you want to search by ingredients? (y = yes, n = no):")
            if answer == "y" or answer == "Y":
                results = searcher.search(q, limit=10,filter = query.Term("ingredients",input("Type in the sepcific ingredient, (if more than one use ',' to separte)\n")))
                #allow_q = query.Term("ingredients",input("Type in the sepcific ingredient, if more than one use ',' to separte"))
                break
            elif answer == "n" or answer == "N":
                results = searcher.search(q, limit=10)
                break
            else:
                print("Wrong answer")

        Store_Matches()
        print_result(results)



    # # index searcher object
    # with ix.searcher() as searcher:
    #     # search() takes a whoosh.query.Query object and returns a Results object
    #     '''Note: We will need to limit the result for recipe (around 5 to 10) (Discuss 1,5,10)
    #     Note: it looks like that we can only read the results from here, 
    #     otherwise it will say that the reader is closed'''

    #     results = searcher.search(q, limit=10,filter = allow_q)
    #     Store_Matches()
    #     print_result(results)
