# Module for all displaying functions
import os
from sys import platform  # Determine what os for the clear command.

clear_command = ""

if (platform == "win32"):
    clear_command = "cls"
elif (platform == "linux" or platform == "darwin"):
    clear_command = "clear"


def display_todos(data: dict):
    os.system(clear_command)

    symbols = [" ", "~", "✓"]
    for symbol_id, title in enumerate(["TODO", "DOING", "DONE"]):  # Save code by putting this in a list.
        print(f"{title}:")
        for item_id, item in enumerate(data[title.lower()]):
            try:
                print(f"    [{symbols[symbol_id]}] - {item['text']} #{item_id}")
            except:  # This is because of range() giving a IndexError.
                pass
