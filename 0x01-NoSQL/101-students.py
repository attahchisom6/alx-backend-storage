#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    function to retrieve a list of students sorted according to their average
    as they are printed
    """
    top_students = mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}}
        },
        {"$sort": {"averageScore": -1}}
    ])
    return top_students
