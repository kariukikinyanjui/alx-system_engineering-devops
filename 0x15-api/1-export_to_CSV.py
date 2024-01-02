#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
import requests
import sys


def export_to_csv(user_id, user_name, completed_tasks):
    filename = "{}.csv".format(user_id)
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)

        for a in completed:
            csv_writer.writerow(
                    [user_id, user_name, a["completed"], a["title"]])


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    # Retrieve user information
    user = requests.get(api_url + "users/{}".format(user_id))
    user_data = user.json()

    # Retrieve to-do list information
    todos = requests.get(api_url + "todos", params={"userId": user_id})
    todos_data = todos.json()

    # Filter completed tasks
    completed = [task for task in todos_data if task.get("completed")]

    # Print summary
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed), len(todos_data)))

    for a in completed:
        print("\t {}".format(a["title"]))

    # Export to CSV
    export_to_csv(user_id, user_data["name"], completed)
    print("Data exported to {}.".format(user_id + ".csv"))
