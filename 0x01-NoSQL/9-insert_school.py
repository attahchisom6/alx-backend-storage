#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection based on
"""


insert_school(mongo_collection, **kwargs):
    """
    function returning the id of an inserted document
    """
    docmt = mongo_collection.insert_one(kwargs)
    return docmt.inserted_id
