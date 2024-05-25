#!/usr/bin/env python3
"""log stats from collection
"""
from pymongo import MongoClient


def log_stats():
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)
    db = client.logs
    collection = db.nginx

    # Count total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count documents by HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count documents with method GET and path /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
