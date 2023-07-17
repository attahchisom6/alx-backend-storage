#!/usr/bin/env python3
"""
main
"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.db_name.school
    newDocID = insert_school(school_collection, name="MoseForGod", address="naijaLand")
    print("inserted new document_id: {}".format(newDocID))
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get("_id"), school.get("name")))
