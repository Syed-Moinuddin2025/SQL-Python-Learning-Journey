from pymongo import MongoClient

# Replace <db_password> with your actual password
conn_str = "mongodb+srv://syed_moin:Sm$$9911@mydbcluster.n1bukn1.mongodb.net/?retryWrites=true&w=majority&appName=MyDBCluster"

# Connect to MongoDB Atlas
client = MongoClient(conn_str)

# Select database and collection
db = client["test_database"]
collection = db["users"]

# Insert sample data
sample_user = {
    "name": "Syed Moin",
    "email": "syed@example.com"
}
insert_result = collection.insert_one(sample_user)
print(f"✅ Inserted with ID: {insert_result.inserted_id}")

# Read all documents
print("\n📋 All Users in Collection:")
for doc in collection.find():
    print(doc)
