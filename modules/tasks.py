# Module for handling and outputing tasks commands.

import json


def json_save(data: dict):
    with open("data/data.json", "w") as f:
        json.dump(data, f, indent=4)


# For handling user input and doing the right function for the command
def handle_commands(task_input: str, task_data: dict):
    if (task_input == "0"):
        exit()

    elif (task_input == "1" or task_input.lower() == "add"):
        add_task(data=task_data)

    elif (task_input== "2" or task_input.lower() == "move"):
        move_task(data=task_data)

    elif (task_input== "3" or task_input.lower() == "clearcat"):
        clear_category(data=task_data)

    elif (task_input == "4" or task_input.lower() == "clearall"):
        clear_all(data=task_data)


def add_task(data: dict):
    print("\nAdd Task:")
    print("Structure: <category> <text> (Example: doing Update README.md)")
    task_input = input("[*] Task: ")
    task_input = task_input.split(" ", 1)

    try:
        category, text = task_input[0], task_input[1]
    except IndexError as e:
        print(e)
        return


    if (category.lower() == "todo"):
        data["todo"].append({"text": text, "category": category})

    elif (category.lower() == "doing"):
        data["doing"].append({"text": text, "category": category})

    elif (category.lower() == "done"):
        data["done"].append({"text": text, "category": category})

    json_save(data=data)


def move_task(data: dict):
    print("\nAdd Task:")
    print("Structure: <item's category> <item id> <category to move too> (Example: todo 0 doing)")
    task_input = input("[*] Task: ")
    task_input = task_input.split(" ")

    try:
        item_category, item_id, new_category = task_input[0].lower(), int(task_input[1]), task_input[2].lower()

        data[new_category].append(data[item_category][item_id])
        del data[item_category][item_id]

    except Exception as e:  # Error when choosen id that doens't exist
        print(e)

    json_save(data=data)


def clear_category(data: dict, manual_category=" "):
    if (manual_category != " "):  # For clear_all()
        data[manual_category].clear()
        return

    print("\nAdd Task:")
    print("Structure: <category>")
    category_input = input("[*] Category: ").lower()

    try:
        data[category_input].clear()
    except KeyError as e:  # When the category choosen is unknown
        print(e)

    json_save(data=data)


def clear_all(data: dict):
    clear_category(data=data, manual_category="todo")
    clear_category(data=data, manual_category="done")
    clear_category(data=data, manual_category="doing")

    json_save(data=data)
