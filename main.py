from modules.display import *
from modules.tasks import *
import json


with open("data/data.json", "r") as f:
    task_data = json.load(f)


# Loading any previously existing tasks.
task_todo = [task_data["todo"]]
task_doing = [task_data["doing"]]
task_done = [task_data["done"]]


if __name__ == "__main__":
    while True:
        display_todos(data=task_data)
        print(task_data)
        print("\n[1] - Add new todo")
        print("[2] - Move existing todo")
        print("[3] - Clear every todo")
        print("[4] - Clear every todo in a certain category")
        print("[0] - Exit\n")

        user_input = input("Input: ").lower()
        handle_commands(task_input=user_input, task_data=task_data)




    