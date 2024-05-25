#!/usr/bin/env python3
"""pymongo"""


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a mongo collection"""
    new_documents = mongo_collection.insert(kwargs)
    return new_documents
