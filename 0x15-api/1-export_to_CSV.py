#!/usr/bin/python3
"""
A script that using REST API for a given employee ID, exports information
about his/her TODO list progress in CSV format.
"""
import csv
import requests
import sys


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

    # Define CSV file name
    csv_file_name = "{}.csv".format(user_id)

    # Write data to CSV file
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
