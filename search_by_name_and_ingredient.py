from __future__ import print_function
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

#User Menu
def PrintMenu():
    print("---------------------")
    print("Type '1' for search by recipe name")
    print("Type '2' for seach by ingredient")
    print("Type '0' to end")



# Store the results, id and recipe name into two list
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
    
    #Store the results
    for hit in results:
        Hitted_ids.append(hit['id'])
        Hitted_recipe_names.append(hit["name"])
        Hitted_ingredients.append(hit["ingredients"])
        Hitted_nutri.append(hit["nutri_info"])

#Print the results
def print_result(results):
    
    # print the mactched recipe id and the name of the recipes (range(len(results)))
    print("----------------------------------")
    print("Matched results,\n#.( Recipe name, ingredients, nutritional data)")

    for hit in range(0, len(Hitted_recipe_names)):
        print(str(hit+1) + "." +
            "(" + Hitted_ids[hit] + "," + "name:" + Hitted_recipe_names[hit] + ", ingredients " + Hitted_ingredients[hit] + ", nutritional data" + Hitted_nutri[hit] + ")")

    # print the stats
    print("----------------------------------")
    print("The stats")
    print("number of results:", len(results))
    print("Searching stats:", results)

# Search by fields
def sTool(first, second):
    
    #Infinite loop to avoid reading json repetitively 
    open = True
    while(open):
        
        # takes in name of the default field to search, and the name of the schema
        qp = QueryParser(first, schema=ix.schema)
        print("--------------------------\nType 0 if you want to go to menu.")
        user_query = input("Search by " + first + ": ")
        if user_query == '0':
            print("Thank you for using the search tool")
            break

        q = qp.parse(user_query)
        
        # index searcher object
        with ix.searcher() as searcher:

            while(True):
                answer = input("Do you want to search by "+ second+ " ? (y = yes, n = no):")
                if answer == "y" or answer == "Y":
                    results = searcher.search(q, limit=10,filter = query.Term(second,input("Type in the sepcific " + second + ", (if more than one use ',' to separte)\n")))
                    break
                elif answer == "n" or answer == "N":
                    results = searcher.search(q, limit=10)
                    break
                else:
                    print("Wrong answer")

            Store_Matches(results)
            print_result(results)



# schema = Schema(
#     ingredients=TEXT(stored=True),
#     url=ID(stored=True),
#     partition=TEXT(stored=True),
#     title=TEXT(stored=True),
#     id=ID(stored=True),
#     instructions=TEXT(stored=True)
# )

# set up schema
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
x = open('/Users/maxwang/Desktop/json/recipes_with_nutritional_info.json')
layer1 = json.load(x)
for i in range(0, len(layer1)):
    ingredients1 = ""
    for j in range(0,len(layer1[i]["ingredients"])):
        ingredients1 += layer1[i]["ingredients"][j]["text"]
    writer.add_document(name=layer1[i]["title"], id=layer1[i]["id"],ingredients = ingredients1,
    nutri_info = str(layer1[i]["nutr_values_per100g"]))

writer.commit()

# get chocie
while(True):
    
    #Print menu
    PrintMenu()
    user_choice = input("choice:")
    
    #Seach by name first
    if user_choice == "1":
        sTool("name", "ingredients")
    
    #Search by ingredient first
    elif user_choice == "2":
        sTool("ingredients","name")
    
    #end the search
    elif user_choice == "0":
        break
    else:
        print("wrong answer")
