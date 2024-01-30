#!/usr/bin/python3
"""
Import Modules HERE
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    all_todos = {}

    for user in users:
        tasks = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {
                        "username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')
                        }
                tasks.append(task_dict)
        all_todos[user.get('id')] = tasks

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(all_todos, file)
