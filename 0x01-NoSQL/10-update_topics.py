#!/usr/bin/env python3
"""
Python function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    function to update all documents with a given name in a collection
    to a specified ropic
    Args:
        mongo_collection: pymongo collectiion objects
        name: school name to update
        topic: list of strings of topic stidied in the school
    """
    mongo_collection.update_many(
            {"name":name},
            {"$set": {"topics": topics})
