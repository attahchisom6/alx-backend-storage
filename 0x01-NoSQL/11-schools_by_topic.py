#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    function to return a list of school that studies a given topic

    Args:
        mongo_collection: this will be the pymongo collection object
        topic (string): this will be topic searched
    """
    return list(mongo_collection.find({"topic": topic}))
