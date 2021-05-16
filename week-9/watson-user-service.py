# ==================================================
# Title: Exercise 9.2 - Querying and Creating Documents
# Author: Professor Krasso
# Date: 16 May 2021
# Modified By: Mark Watson
# Description: This program shows how to create and query a
#    document in MongoDB with Python.
# ==================================================

# import required modules
from pymongo import MongoClient
import pprint
import datetime

# connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.web335

# create document
user = {
  "first_name": "Jack",
  "last_name": "Kruse",
  "email": "krusej@email.com",
  "employee_id": "2025810",
  "date_created": datetime.datetime.utcnow()
}

# insert document to mongoDB users collection
user_id = db.users.insert_one(user).inserted_id

# print generated _id
print(user_id)

# find user by employee_id and print
pprint.pprint(db.users.find_one({"employee_id": "2025810"}))
