#!/usr/bin/env python3
"""
this module is responsible find topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Filters schools in the collection based on the specified topic.

    Args:
        mongo_collection: The MongoDB collection to query.
        topic (str): The topic to filter schools by.

    Returns:
        List[dict]: A list of documents (schools) that contain field.
    """
    xxx = mongo_collection.find({"topics": topic})

    return list(xxx)
