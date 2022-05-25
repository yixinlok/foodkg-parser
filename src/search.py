
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
import os.path
import os
from whoosh.qparser import QueryParser

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
    name=TEXT(),
    id=ID
)

# create an index object
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
# get index writer object
writer = ix.writer()

# add documents to index
# later we will loop through the json and add each list entry as a document here
writer.add_document(name=u"mac and cheese", id=u"2395230")
writer.add_document(name=u"cheesecake", id=u"32523953")
writer.add_document(name=u"apple pie", id=u"23523523")
writer.commit()


# takes in name of the default field to search, and the name of the schema
qp = QueryParser("name", schema=ix.schema)
q = qp.parse(u"apple")

# index searcher object
with ix.searcher() as searcher:
    # search() takes a whoosh.query.Query object and returns a Results object
    results = searcher.search(q, limit=None)

# The Results object acts like a list of the matched documents. You can use it to access the stored fields of each hit document, to display to the user.
print("number of results:")
print(len(results))
print(results)
