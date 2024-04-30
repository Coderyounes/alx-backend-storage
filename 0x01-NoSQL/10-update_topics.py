#!/usr/bin/env python3
""" Documentation """


def update_topics(mongo_collection, name, topics):
    """
    Update the 'topics' field of documents in the given MongoDB collection
    that match the specified 'name' with the provided 'topics' list.

    Args:
        mongo_collection: The MongoDB collection to update.
        name (str): The name to match documents by.
        topics (list): The new list of topics to set.

    Returns:
        None
    """
    mongo_collection.update_many({'name': name}, {"$set": {'topics': topics}})
