#!/usr/bin/env python3
"""
8-all.py
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of documents in the collection.
    """
    return mongo_collection.find()
