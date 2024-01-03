#!/usr/bin/python3
"""
A script that, using REST API for a given employee ID, exports information
about his/her TODO list progress in JSON and CSV formats.
"""
import csv
import json
import requests
import sys


def export_to_csv(user_id, user, todos):
    csv_file_name = "{}.csv".format(user_id)
    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = [
                "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames,
                quoting=csv.QUOTE_ALL, quotechar='"'
                )

        writer.writeheader()

        # Write each task's information to the CSV file
        for task in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user.get("username"),
                "TASK_COMPLETED_STATUS": str(task.get("completed")),
                "TASK_TITLE": task.get("title")
                })
    print("CSV file '{}' has been created.".format(csv_file_name))


def export_to_json(user_id, user, todos):
    json_data = {
            user_id: [
                {
                    "task": task.get("title"), "completed": task.get(
                        "completed"), "username": user.get("username")
                    }
                for task in todos
                ]
            }
    json_file_name = "{}.json".format(user_id)
    with open(json_file_name, mode='w') as json_file:
        json.dump(json_data, json_file)
    print("JSON file '{}' has been created.".format(json_file_name))


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    # Fetch user information
    user_response = requests.get(api_url + "users/{}".format(user_id))
    user = user_response.json()

    # Fetch TODO list for the user
    todos_response = requests.get(
            api_url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    export_to_csv(user_id, user, todos)
    export_to_json(user_id, user, todos)
