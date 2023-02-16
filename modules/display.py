# Module for all displaying functions
import os
from sys import platform  # What os for clear command.

clear_command = ""

if (platform == "win32"):
    clear_command = "cls"
elif (platform == "linux" or platform == "darwin"):
    clear_command = "clear"



def display_todos(data: dict):
    os.system(clear_command)

    dict_num = 0
    symbols = [" ", "~", "✓"]
    for symbol_id, title in enumerate(["TODO", "DOING", "DONE"]):  # Save code by putting this in a list.
        print(f"{title}:")
        for item in data[title.lower()]:
            try:
                print(f"    [{symbols[symbol_id]}] - {item['text']}")
            except:  # This is because of range() giving a IndexError.
                pass
                 
        dict_num += 1  # Updating dict_num to move onto next item in the list.

