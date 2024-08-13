#!/usr/bin/env python3
"""
Script to insert documents into a MongoDB collection.
"""
from typing import Any


def insert_school(mongo_collection, **kwargs) -> Any:
    """
    Inserts a document into the specified MongoDB collection.

    Args:
        mongo_collection: The MongoDB collection where document be inserted.

    Returns:
        The unique identifier (_id) of the inserted document.
    """
    insert_data = mongo_collection.insert_one(kwargs).inserted_id

    return insert_data
