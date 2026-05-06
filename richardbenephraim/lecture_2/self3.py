"""
To-Do List Application
Write a program to create a simple To-Do List application. The program allows
users to add tasks, view the current list of tasks, and remove tasks once they are
completed.

"""

import json
from json import JSONDecodeError

def main():
     front_logic()


# a function to save the file
def save_file(data):
    
    with open ("data.json", "w", encoding="utf-8") as file:
        save_data =  json.dump(data, file, indent=4)

    return save_data



#a function to load the file
def load_file():
    
    try:
        with open ("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except (JSONDecodeError, FileNotFoundError):
        data = [] 

    return data

#this is the control function
def front_logic():
    head = f"*"*5 + " TODO list Menu " + f"*"*5
    
    while True:
        message = input(
        f"\n {head} \n"
        "1: View Tasks\n"
        "2: Add a New Task\n"
        "3: Remove a Task\n"
        "4: exit program\n"
        "\nEnter your choice: \n"
    ).strip()

    
        match message:
            case "1":
                data = load_file()
                if len(data) == 0:
                    print("list is empty")
                    
                else:
                    data
                    print()
                    for index, item in enumerate(data, 1):
                        print(f'{index}: {item}')
                    print("\nitems listed successfully\n")

                    
            case "2":
                todo_data = input("Enter a new task: \n")
                data = load_file()
                data.append(todo_data)
                save_file(data)
                print("item added successfully")
                
            case "3":
                todo_data = input("enter of item to be removed: \n")
                data = load_file()
                try:

                    data.remove(todo_data)
                except (TypeError, ValueError) as e:
                    print("item not found in list")
                    print(f"error: {e}")
                save_file(data)

            case "4":
                print("program exited")
                break
            case _:
                print("invalid user choice")
                continue
        print()

if __name__ == "__main__":
    main()