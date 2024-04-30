#!/usr/bin/env python3
""" Documentation """


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve schools from a MongoDB collection based on a given topic.

    Args:
        mongo_collection: The MongoDB collection to query.
        topic (str): The topic to filter schools by.

    Returns:
        A cursor object containing the schools matching the given topic.
    """
    return mongo_collection.find({"topics": topic})
