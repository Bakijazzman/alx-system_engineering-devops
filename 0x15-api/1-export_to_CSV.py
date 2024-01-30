#!/usr/bin/python3
"""
Import Docs here
"""
import csv
from sys import argv
import requests

if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_str = f'{url}users/{user_id}'
    todos_str = f'{url}todos?userId={user_id}'
    file = f'{user_id}.csv'

    response = requests.get(user_str)
    username = response.json().get('username')

    response = requests.get(todos_str)
    tasks = []
    for task in response.json():
        tasks.append([user_id, username,
                     task.get('completed'), task.get('title')])
    with open(file, mode='w') as emp_file:
        emp_writer = csv.writer(emp_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in tasks:
            emp_writer.writerow(task)
