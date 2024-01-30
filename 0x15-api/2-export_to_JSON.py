#!/usr/bin/python3
"""
Import Modules Here
"""
import json
from sys import argv
import requests

if __name__ == "__main__":
    user_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(url)
    todos = requests.get(todos_url)
    todos_user = {}
    tasks = []
    for task in todos.json():
        if task.get('userId') == int(user_id):
            task_dict = {
                    "task": task.get("title"),
                    "completed": task.get('completed'),
                    "username": user.json().get('username')
                    }

            tasks.append(task_dict)
        todos_user[user_id] = tasks
    file = user_id + ".json"

    with open(file, mode='w') as user_file:
        json.dump(todos_user, user_file)
