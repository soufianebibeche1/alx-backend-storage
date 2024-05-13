#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (string): The topic to search for.

    Returns:
        A list of schools with the specified topic.
    """

    return mongo_collection.find({"topics": topic})
