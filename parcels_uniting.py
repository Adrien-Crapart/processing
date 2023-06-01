import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database called "mydatabase"
mydb = myclient["mydatabase"]

# Return a list of your system's databases
print(myclient.list_database_names())

# Check if "mydatabase" exists
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

# Create a collection called "customers"
mycol = mydb["customers"]

# Return a list of all collections in your database
print(mydb.list_collection_names())

# Check if the "customers" collection exists
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

# Insert a record in the "customers" collection
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)

# Find the first document in the customers collection
x = mycol.find_one()
print(x)

# Return all documents in the "customers" collection
for x in mycol.find():
  print(x)

# Return only the names and addresses, not the _ids
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

# Find document(s) with the address "Park Lane 38"
myquery = { "address": "Park Lane 38" }
# Find documents where the address starts with the letter "S" or higher
myquery = { "address": { "$gt": "S" } }
# Find documents where the address starts with the letter "S"
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

# Sort the result alphabetically by name
mydoc = mycol.find().sort("name",1)
mydoc = mycol.find().sort("name",-1)
for x in mydoc:
  print(x)

# Delete the document with the address "Mountain 21"
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)
# Delete all documents were the address starts with the letter S
x = mycol.delete_many(myquery)
# Delete all documents in the "customers" collection
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

# Delete the "customers" collection
mycol.drop()