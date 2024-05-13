#!/usr/bin/env python3
"""
9-insert_school.py
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Keyword arguments representing the fields of the document.

    Returns:
        The new _id of the inserted document.
    """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
