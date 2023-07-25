#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
import sys


def get_todo_list_progress(employee_id):
    total_task = 0
    completed_task = 0

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    employee = requests.get(url).json()
    todos = requests.get(f"{url}/todos").json()

    employee_name = employee['name']

    for todo in todos:
        total_task += 1
        if todo['completed']:
            completed_task += 1

    print(f"employee {employee_name} is done with tasks({completed_task}/{total_task}):")
    
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide an employee ID as a parameter.")
    else:
        employee_id = sys.argv[1]
        get_todo_list_progress(employee_id)