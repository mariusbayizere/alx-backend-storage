#!/usr/bin/env python3
"""
Script to update the 'topics' field of documents in a collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all documents collection specified value.

    Args:
        mongo_collection: The MongoDB collection in which to  update.
        name (str): The value of the 'name' field to match documents.
        topics (list): The new list of topics to set for matched documents.

    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
