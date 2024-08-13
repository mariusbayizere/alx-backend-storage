#!/usr/bin/env python3
""" 101-main """

from pymongo import MongoClient

# Import functions from other modules
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
top_students = __import__('101-students').top_students

if __name__ == "__main__":
    # Connect to MongoDB
    mongo_client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = mongo_client.my_db.students

    # Define a list of students with their topics and scores
    students_data = [
        {
            'name': "John",
            'topics': [
                {'title': "Algo", 'score': 10.3},
                {'title': "C", 'score': 6.2},
                {'title': "Python", 'score': 12.1}
            ]
        },
        {
            'name': "Bob",
            'topics': [
                {'title': "Algo", 'score': 5.4},
                {'title': "C", 'score': 4.9},
                {'title': "Python", 'score': 7.9}
            ]
        },
        {
            'name': "Sonia",
            'topics': [
                {'title': "Algo", 'score': 14.8},
                {'title': "C", 'score': 8.8},
                {'title': "Python", 'score': 15.7}
            ]
        },
        {
            'name': "Amy",
            'topics': [
                {'title': "Algo", 'score': 9.1},
                {'title': "C", 'score': 14.2},
                {'title': "Python", 'score': 4.8}
            ]
        },
        {
            'name': "Julia",
            'topics': [
                {'title': "Algo", 'score': 10.5},
                {'title': "C", 'score': 10.2},
                {'title': "Python", 'score': 10.1}
            ]
        }
    ]

    # Insert students into the collection
    for student in students_data:
        insert_school(students_collection, **student)

    # Retrieve and print all students
    all_students = list_all(students_collection)
    for student in all_students:
        print("[{}] {} - {}".format(
            student.get('_id'),
            student.get('name'),
            student.get('topics')
        ))

    # Retrieve and print top students
    best_students = top_students(students_collection)
    for student in best_students:
        print("[{}] {} => {}".format(
            student.get('_id'),
            student.get('name'),
            student.get('averageScore')
        ))
