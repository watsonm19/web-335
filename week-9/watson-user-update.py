# ==================================================
# Title: Exercise 9.3 - Updating and Deleting Documents
# Author: Professor Krasso
# Date: 16 May 2021
# Modified By: Mark Watson
# Description: This program shows how to update a
#    document in MongoDB with Python.
# ==================================================

# import required modules
from pymongo import MongoClient
import pprint
import datetime

# connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.web335

# updates employee document in mongoDB users collection
db.users.update_one(
  {"employee_id": "2025810"},
  {
    "$set": {
      "email": "marwatson@my365.bellevue.edu"
    }
  }
)

# prints updated document
pprint.pprint(db.users.find_one({"employee_id": "2025810"}))
