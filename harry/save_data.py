import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import json 
import os 

def save_data():
    # Collect data from Tkinter widgets
    name = entry_name.get()
    sex = var_sex.get()
    course = combo_course.get()
    address = text_address.get("1.0", "end-1c")

    new_stud_info = {
        "name":name, 
        "sex":sex, 
        "course":course,
        "address":address
    }
    #to check wether the file exist 
    filename = 'student_data.json'
    if os.path.exists(filename):
        #read the existing file 
        with open(filename, 'r') as read_file:
            student_info = json.load(read_file)
            

    else:
        #create a new file and setup the basic format for a json file 
        student_info = {"student_information":[]}
        with open(filename, 'w') as create_file:
            json.dump(student_info, create_file, indent=3)

    student_info["student_information"].append(new_stud_info)
    with open(filename, 'w') as update_file:
        json.dump(student_info,update_file, indent=4 )
    messagebox.showinfo("STUDENT INFO", "DATA SAVED SUCCESSFULLY")



# Create a Tkinter window
root = tk.Tk()
root.title("Send Data to JSON")

# Widgets for collecting data
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_sex = tk.Label(root, text="Sex:")
label_sex.grid(row=1, column=0, padx=5, pady=5)
var_sex = tk.StringVar()
radio_male = tk.Radiobutton(root, text="Male", variable=var_sex, value="Male")
radio_female = tk.Radiobutton(root, text="Female", variable=var_sex, value="Female")
radio_male.grid(row=1, column=1, padx=5, pady=5)
radio_female.grid(row=1, column=2, padx=5, pady=5)

label_course = tk.Label(root, text="Course:")
label_course.grid(row=2, column=0, padx=5, pady=5)
course_offered = ["information technology","accountancy","hotel and restaurant"]
combo_course = ttk.Combobox(root,values=course_offered)
combo_course.grid(row=2, column=1, padx=5, pady=5)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0, padx=5, pady=5)
text_address = tk.Text(root, height=4, width=30)
text_address.grid(row=3, column=1, padx=5, pady=5)

# Button to save data
btn_save = tk.Button(root, text="Save Data", command=save_data)
btn_save.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()