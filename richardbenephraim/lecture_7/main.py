
"""
 Biuld a simple UI with tkinter to take student form and save
 TODO =>
 use OOP 
"""


from os import listdir, path
import os
import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk, font
from json import JSONDecodeError, load, dump




class StudentRegistrationForm:
    if not path.exists("file"):
     os.mkdir("file")
    data_path = path.join("file", "config.json")
    
    try:
            with open (file=data_path, mode="r", encoding="utf-8") as file:
                configFile = load(file)
    except (JSONDecodeError, FileNotFoundError, FileExistsError):
                configFile = []
        
        

    def __init__(self):
        
        self.on_clickSubmit
        # main window settings

        self.root = tk.Tk()
        self.root.geometry("500x600")
        self.root.title("Student Registration Form")
        self.root.configure(bg="#af7eea")
        
        self.masterFont = font.Font(family="Arial ",size=15, weight="bold") # i will use this a custom font object
        self.checkboxint = tk.IntVar()

        self.userFirstName_label = tk.Label(self.root, text= "First Name",foreground="#ffffff",bg="#af7eea",font=self.masterFont)
        self.userFirstName_label.pack(padx=5, pady=5)

        self.userFirstName_entry = tk.Entry(self.root)
        self.userFirstName_entry.pack(padx=5)

        self.userLastName_label = tk.Label(self.root, text= "Last Name",foreground="#ffffff",bg="#af7eea",font=self.masterFont)
        self.userLastName_label.pack(padx=5, pady=5)

        self.userLastName_entry = tk.Entry(self.root)
        self.userLastName_entry.pack(padx=5)




        self.userEmail_label = tk.Label( self.root, text= "Email",foreground="#ffffff",bg="#af7eea",font=self.masterFont)
        self.userEmail_label.pack()


        self.userEmail_entry = tk.Entry(self.root)
        self.userEmail_entry.pack()

        self.userPhone_label = tk.Label( self.root, text= "Phone Number",foreground="#ffffff",bg="#af7eea",font=self.masterFont)
        self.userPhone_label.pack()


        self.userPhone_entry = tk.Entry(self.root)
        self.userPhone_entry.pack()
                                   

        self.userLocation_label = tk.Label( self.root, text= "Location",foreground="#ffffff",bg="#af7eea",font=self.masterFont)
        self.userLocation_label.pack()


        self.userLocation_entry = tk.Entry(self.root)
        self.userLocation_entry.pack()
                                   

        self.userUsername_label = tk.Label( self.root, text= "Username",foreground="#ffffff",bg="#af7eea",font=self.masterFont)
        self.userUsername_label.pack()


        self.userUsername_entry = tk.Entry(self.root)
        self.userUsername_entry.pack()


        self.userPassword_label = tk.Label(self.root, text="Password", foreground="#ffffff",bg="#af7eea",font=self.masterFont)
        self.userPassword_label.pack()                               

        self.userPassword_entry = tk.Entry(self.root)
        self.userPassword_entry.pack()    


        self.submitButton = tk.Button(self.root, text= "Submit", bg="#ff2200", command=self.on_clickSubmit)  
        self.submitButton.pack(pady=10)    


        self.root.mainloop()






    def on_clickSubmit(self):
        self.fname = self.userFirstName_entry.get()
        self.lname = self.userLastName_entry.get()
        self.email = self.userEmail_entry.get()
        self.phone = self.userPhone_entry.get()
        self.location = self.userLocation_entry.get()
        self.username = self.userUsername_entry.get()
        self.password = self.userPassword_entry.get()


        if self.fname and self.lname and self.email and self.phone and self.location and self.username and self.password:
            messagebox.showinfo(title="Success", message="Data Successfully Submitted")
        else:
            messagebox.showwarning(title="Error", message="Fill all space")
    

        self.data_appended = {
            "UUID" : next(self.dd),
            "first name" : self.fname,
            "last name" : self.lname,
            "email" : self.email,
            "phone" : self.phone,
            "location" : self.location,
            "username" : self.username,
            "password" : self.password
        }    

        self.configFile.append(self.data_appended)
        self.save_data_to_json(self.configFile)


    

    def save_data_to_json(self, data_appended):

        with open(self.data_path, mode="w", encoding="utf-8") as file:
            dump(data_appended, file, indent=4)

    def id_generation():
        

         c = 100
         while c > 0:
            
            yield c
            c +=1
      
    dd = id_generation()



    
     

    
    

         

         


    


forms = StudentRegistrationForm()

