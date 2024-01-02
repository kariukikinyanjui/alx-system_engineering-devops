#!/usr/bin/python3
"""
Script that, using a REST API for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

        employee_id = int(sys.argv[1])

        # Fetch user data
        user_response = requests.get(
                "https://jsonplaceholder.typicode.com/users/{}".format(
                    employee_id))
        todos_response = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                    employee_id))

        user_data = user_response.json()
        todos_data = todos_response.json()

        # Extract relevant information
        employee_name = user_data.get("name")
        done_tasks = [task for task in todos_data if task.get("completed")]
        total_tasks = len(todos_data)
        done_tasks_count = len(done_tasks)

        # Display information
        print(
                "Employee {} is done with tasks({}/{}:".format(
                    employee_name, done_tasks_count, total_tasks
                    )
                )
        for task in done_tasks:
            print("\t{}".format(task.get("title")))
