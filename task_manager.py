'''
Docstring for python_practice.task_manager.task_manager

The "State Manager" (File I/O & JSON)
The Assignment: Create a command-line "Task Manager."

The Goal: Build a script that lets you add tasks via the terminal (python tasks.py add "Buy milk") and saves them to a tasks.json file.

Why it matters: Senior engineers rarely keep data in memory. You must master serialization (converting Python dicts to JSON) and deserialization (loading them back) so your "Scraper" can resume after a crash.

Mastery Check: Can your script handle a corrupted JSON file without crashing? (Hint: Use try/except).
'''

import json

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