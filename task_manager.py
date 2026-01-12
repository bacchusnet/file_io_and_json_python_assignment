'''
Docstring for python_practice.task_manager.task_manager

The "State Manager" (File I/O & JSON)
The Assignment: Create a command-line "Task Manager."

The Goal: Build a script that lets you add tasks via the terminal (python tasks.py add "Buy milk") and saves them to a tasks.json file.

Why it matters: Senior engineers rarely keep data in memory. You must master serialization (converting Python dicts to JSON) and deserialization (loading them back) so your "Scraper" can resume after a crash.

Mastery Check: Can your script handle a corrupted JSON file without crashing? (Hint: Use try/except).
'''

import json
import logging
import sys


logging.basicConfig(
    level=logging.INFO, # Set the minimum level to log (INFO, DEBUG, WARNING, etc.)
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)


def add_stuff(a: int, b: int):
    return a + b


def read_file():
    try:
        with open('./tasks,json', 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            tasks_list = tasks.get('List', [])
    except:
        print("some error")

    return tasks_list


def write_file(data, user_input):
    try:
        with open('./tasks.json', 'r', encoding='utf-8') as file:
            data.append(user_input)
            data_json = {"List": data}
            json.dump(data_json, file)
    except:
        print('error')
        
    return "Successfully wrote to file."


def main():

    while True:
        user_input = input("Enter something...\n")

        if user_input == "exit":
            print("Exiting program...Goodbye")
            break
        else:
            try:
                with open('./tasks.json', 'r', encoding='utf-8') as file:
                    tasks = json.load(file)
                    tasks_list = tasks.get('List', [])

                with open('./tasks.json', 'w', encoding='utf-8') as file:
                    tasks_list.append(user_input)
                    tasks_json = {"List": tasks_list}
                    json.dump(tasks_json, file)

            except FileNotFoundError:
                print('error occured file not found')   
            except json.JSONDecodeError as e:
                print(f"Error: Failed to decode JSON from the file: {e}")


if __name__ == "__main__":
    main()