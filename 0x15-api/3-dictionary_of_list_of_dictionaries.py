#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    # Make the GET request
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    # Organize tasks by user ID
    tasks_by_user = {}
    todos = response.json()
    for task in todos:
        user_id = task["userId"]
        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []

        tasks_by_user[user_id].append({
            "username": task.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
            })

    # Create a JSON file with all tasks
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file, indent=4)
