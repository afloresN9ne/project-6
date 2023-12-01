import os
from pymongo import MongoClient
import logging

# Set up MongoDB connection
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

# Use database "todo"
db = client.mydb

# Use collection "lists" in the databse
collection = db.lists


def insert_db(brevet_distance,start_date,times):
    '''
    saves brevet_dist,start date, control_brevets, open and close times 
    to a database 
    '''
    output = collection.insert_one({
        "brevet_distance": brevet_distance,
        "start_date":start_date,
        "times":times})
    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)

def fetch_db():
    
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    lists = collection.find().sort("_id", -1).limit(1)

    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:
    for db_list in lists:
        # We store all of our lists as documents with two fields:
        ## title: string # title of our to-do list
        ## items: list   # list of items:

        ### every item has two fields:
        #### desc: string   # description
        #### priority: int  # priority
        return db_list["brevet_distance"], db_list["start_date"],db_list["times"],

