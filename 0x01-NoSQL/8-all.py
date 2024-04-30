#!/usr/bin/env python3
""" Documentation """


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.

    Args:
        mongo_collection : The MongoDB collection.

    Returns:
        list: A list of all documents in the collection.
    """
    db_list = []
    if mongo_collection is None:
        return db_list
    else:
        cursor = mongo_collection.find()
        for doc in cursor:
            db_list.append(doc)
        return db_list
