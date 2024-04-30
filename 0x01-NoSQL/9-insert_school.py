#!/usr/bin/env python3
""" Documentation """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a school document into the specified MongoDB collection.

    Args:
        mongo_collection: The MongoDB collection to insert the document into.
        **kwargs: The key-value pairs representing
        the fields and values of the school document.

    Returns:
        str: The inserted document's ID.

    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
