#!/usr/bin/env python

import os
import pickle
import User

# help(os)
# path = os.chdir('/home/')
# print(path)

users = [
    {
        "name": 'Gaetan',
        "age": 36
    },
    {
        "name": 'Elise',
        "age": 25
    }
]

with open('user.db', 'wb') as db_file:
    db = pickle.Pickler(db_file)
    db.dump(users)

with open('user.db', 'rb') as db_file:
    db = pickle.Unpickler(db_file)
    data = db.load()

# print(data)

for i, element in enumerate(data):
    print('{} a {} ans'.format(element['name'], str(element['age'])))
