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
    schools_by_topic = []
    cursor = mongo_collection.find({"topics": topic})
    for school in cursor:
        schools_by_topic.append(school)
    return schools_by_topic
