#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection based on
"""


def insert_school(mongo_collection, **kwargs):
    """
    function returning the id of an inserted document
    """
    document = mongo_collection.insert_one(kwargs)
    document.inserted_id
