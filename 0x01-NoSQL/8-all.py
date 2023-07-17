#!/usr/bin/env python3
"""
script that serve to list all document in a collection
"""


def list_all(mongo_collection):
    """
    function that take a pymongo object and list all document in it else
    an empty list is returned
    """
    documents=  mongo_collection.find()
    return [document for in documents]
