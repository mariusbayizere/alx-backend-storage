#!/usr/bin/env python3
"""
Module to retrieve and list all documents from a MongoDB collection.
"""
from typing import List


def list_all(mongo_collection) -> List[object]:
    """
    Retrieves all documents from the specified MongoDB collection.

    Args:
        mongo_collection: The MongoDB collection from retrieve documents.

    Returns:
        A list of documents found in the collection.
        Returns an empty list if no documents are found.
    """
    data = mongo_collection.find()

    if data.count() == 0:
        return []

    return data
