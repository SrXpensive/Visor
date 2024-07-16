from pymongo import MongoClient

MONGO_URI = 'mongodb://root:root@localhost'

client = MongoClient(MONGO_URI)

db = client['teststore']
collection = db['products']

collection.delete_many({"precio":100})
resultado = collection.find()
for r in resultado:
    print(r)

#collection.insert_many([{"nombre": "teclado","precio": 100},{"nombre": "ratón","precio": 200}])