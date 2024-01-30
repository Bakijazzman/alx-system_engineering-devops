#!/usr/bin/python3
"""import Modules Here """
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_str = '{}users/{}'.format(url, user_id)
    todos_str = '{}todos?userId={}'.format(url, user_id)
    employee_str = "Employee {} is done with tasks"

    response = requests.get(user_str)
    print(employee_str.format(response.json().get('name')), end='')

    response = requests.get(todos_str)
    tasks = []
    for task in response.json():
        if task.get('completed') is True:
            tasks.append(task)

    print(f"({len(tasks)}/{len(response.json())})")
    for task in tasks:
        print(f'\t {task.get("title")}')
