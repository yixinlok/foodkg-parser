import json
import pickle

# from whoosh.fields import Schema, TEXT, ID
# from whoosh import index
# import os
# import os.path
# from whoosh import index
# from whoosh import qparser
# from whoosh.qparser import QueryParser


# load the json file, convert to layer1 python dictionary
# later replace with full layer 1 json
x = open('partial_layer1.json')
layer1 = json.load(x)

dbfile = open('partial_layer1pickle', 'ab')
name_to_id = {}

for i in range(0, len(layer1)):
    # print(layer1[i]["title"])
    # print(layer1[i]["id"])
    name = layer1[i]["title"]
    name_to_id[name] = layer1[i]["id"]

pickle.dump(name_to_id, dbfile)
print(name_to_id)
dbfile.close()
