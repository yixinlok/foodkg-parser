import json
import pickle

# later replace with full layer 1 json
x = open('partial_layer1.json')
layer1 = json.load(x)

print(layer1)


dbfile = open('partial_layer1pickle', 'ab')

pickle.dump(layer1, dbfile)
dbfile.close()
