#!/user/bin/python3
"""
A script that using REST API for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos =\
    requests.get(api_url + "todos", params={"userId": sys.argv[1]}).json()
    completed =\
    [task.get("title") for task in todos if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for a in completed:
        print("\t {}".format(a))
