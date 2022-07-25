import pymongo    

myclient = pymongo.MongoClient("mongodb+srv://harish123:harish123@cluster0.csgv5jj.mongodb.net/test")

mydb = myclient["new_db"]
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "new_db" in dblist:
  print("The database exists.")

mycol = mydb["customers"]
print(mydb.list_collection_names())
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)

print(x.inserted_id)

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

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

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

# first document in the customers collection
x = mycol.find_one()
print(x)

#Return all documents in the customers collection
for x in mycol.find():
  print(x)

#Return only the names and addresses, not the _ids:
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

#This example will exclude "address" from the result:
for x in mycol.find({},{ "address": 0 }):
  print(x)

#You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
for x in mycol.find({},{ "name": 1, "address": 0 }):
  print(x)

for x in mycol.find({},{ "name": 1 }):
  print(x)

#Find document(s) with the address "Park Lane 38":
myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)


#make advanced queries you can use modifiers as values in the query object.
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

#To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

#Sort the result alphabetically by name:
mydoc = mycol.find().sort("name")
for x in mydoc:
  print(x)

#descending
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
  print(x)

#Delete the document with the address "Mountain 21":
# If the query finds more than one document, only the first occurrence is deleted.
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)

#Delete all documents were the address starts with the letter S:
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

#Delete all documents in the "customers" collection:
mycol = mydb["customers"]
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")


# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
# The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.
mycol = mydb["customers"]
mycol.drop()

#Change the address from "Valley 345" to "Canyon 123":
mycol = mydb["customers"]
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

#Update all documents where the address starts with the letter "S":
mycol = mydb["customers"]
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")