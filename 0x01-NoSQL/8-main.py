#!/usr/bin/env python3
"""
testing a python function on mongo server
"""
from pymongo import mongoClient
list_all = __import__('8-all').list_all


if __name__ == "__main__":
    client = mongoClient('mongodb://127.0.0.1:27017')
    schoool_collection = client.db.school
    schools = list_all(school_collection)

    for school in schools:
        print("[{}] {}".format(school.get("_id"), school.get("name')))
