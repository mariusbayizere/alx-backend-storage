#!/usr/bin/env python3
"""
This function returns all students sorted by average score.
The average score is calculated
"""


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """displaying all student and sorted by average score"""
    xxx = mongo_collection.aggregate(
        [
            {"$project": {"name": "$name",
             "averageScore": {"$avg": "$topics.score"}}
             },
            {"$sort": {"averageScore": -1}},
        ]
    )

    return xxx
