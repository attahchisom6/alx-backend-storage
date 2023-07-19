#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    execution entry point
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print("{:d} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print("{} status check".format(status_check))

    ips = collection.aggregate(
            [
                {"$group": {"_id": "ip", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
                {"$limit": 10}
            ]
        )
    print("IPs:")
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
