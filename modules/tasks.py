# Module for handling and outputing tasks commands.

import json

# For handling user input and doing the right function for the command
def json_save(data: dict):
    with open("data/data.json", "w") as f:
         json.dump(data, f, indent=4)
    

def handle_commands(task_input: str, task_data: dict):
    if (task_input == "0"):
        exit()

    elif (task_input == "1"):
        add_task(data=task_data)


def add_task(data: dict):
    print("\nStructure: <category> <text> (Example: doing Update README.md)")
    task_input = input("[*] Task: ")
    task_input = task_input.split(" ", 1)
    category, text = task_input[0], task_input[1]

    if (category.lower() == "todo"):
        data["todo"].append({"text": text, "category": category})

    elif (category.lower() == "doing"):
        data["doing"].append({"text": text, "category": category})

    elif (category.lower() == "done"):
        data["done"].append({"text": text, "category": category})
    
    json_save(data=data)

def move_task(data: dict):
    print("\nStructure: <item's category> <item id (like where on the list it is. starts at 0)> <category to move too> (Example: todo 2 doing ")
    task_input = input("[*] Task: ")
    task_input = task_input.split(" ")
    item_category, item_id, new_category = task_input[0], task_input[1], task_input[2]