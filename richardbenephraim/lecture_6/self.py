'''
         ======Simple Text Editor ======
Write a program to create a simple text editor. This program allows users to open
an existing text file or create a new one, edit the content, and then save the
changes by typing the SAVE command.




'''


import os, sys, time

def main():
    
    """
    i will focus on the os module to handle all the file and folder works =>
    create a seperate function for each logic =>
    functions are meant to perform single task and return the data

    TODO == use functional programming 
    sys => i will use exit to log out of the program
    time = > i will use it to sleep my program for some seconds to let user wait smail


    """





    program_header = f"\n{"*"*10} WELCOME TO THE SIMPLE TEXT EDITOR {"*"*10}\n"

    print(program_header)
    text_editor_logic() # this is only function that will be called to run and get needed response







def text_editor_logic():

    message = input(
        "1. View exiting notes\n"
        "2: Add new text\n"
        "3: edit content saved\n"
        "\nEnter the corresponding number to select \n"
    )
    match message:
        case "1":
            load_file_for_view()
            
        case "2":
            save_file()
        case "3":
            return "coming soon..."
        case _:
            return "invalid input"








def get_user_input_file():

    header = f"*"*10+ " Getting started "+ f"*"*10
    message = input(
        f"\n{header}\n"
        "Enter the filename to open or create: \n"
        "(don't add the '.txt' )"
    ).strip().lower()
    file_head = f"{message}.txt"
    
    return file_head








def file_checker():
    file_head = get_user_input_file()

    if os.path.exists(file_head) == True:
        print("file already exist")
    else:
        print(f"{file_head} not found. \n creating new file")
        try:
            os.mknod(file_head)
            print("file created successfully")
        except (FileExistsError, FileNotFoundError):
            print("Sorry error occured")

    return file_head







def text_editor_input():
    
    message = input(
        "Enter your text"
        "\n"
                    )
    save = input("to save file type 'SAVE' or 'EXIT' to cancel:\n ")

    return message, save 








def save_file():
    file_head = file_checker()

    message, save = text_editor_input()
    temporary_memory = ""
    
    if save == "save" or save == "SAVE":
        with open(file_head, "a") as file:
                file.write(message + "\n")
        print ("text successfuly save.")
    elif save == "exit" or save == "EXIT":
         temporary_memory.join(message) + "\n"
         sys.exit()
    else:
        print ("user choice not valid ...")
    return "a mini notebook"









def load_file_for_view():

    print("printing available saved text files.... please wait...")
    time.sleep(0.5)
    path = os.listdir("./")
    for txt in path:
        if txt.endswith(".txt"):
            print(f"- {txt}")
   

    ask_user_file = input("enter text file: \n")
    path_check = os.listdir()

    if ask_user_file in path_check:
        with open(ask_user_file, "r", encoding="utf-8") as file:
            read_file = file.read()
            print(read_file)
    else:
        print("file not found")
    
   





            

if __name__ == "__main__":
    main()