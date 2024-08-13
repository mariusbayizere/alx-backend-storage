#!/usr/bin/env python3
"""
MongoDB operations with Python using pymongo.
"""
from pymongo import MongoClient

if __name__ == "__main__":
    """Connect to MongoDB"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f"{n_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{status_check_count} status check")

    xxx = nginx_collection.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
            {"$project": {"_id": 0, "ip": "$_id", "count": 1}},
        ]
    )

    print("IPs:")
    for xx in xxx:
        ip = xx.get("ip")
        count = xx.get("count")
        print(f"\t{ip}: {count}")
