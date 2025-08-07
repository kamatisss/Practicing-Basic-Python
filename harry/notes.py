from tkinter import * 
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import ttk
import json 
# Create the main window
root = Tk()
root.title("Login")
root.configure(bg="lightsalmon")

# Username label and entry
label_username = Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5)
entry_username = Entry(root)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry
label_password = Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password = Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Login button
btn_login = Button(root, text="Login", command=lambda:login())
btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

def Create_Account_Window(): 
    cwindow = Toplevel() 
    cwindow.mainloop()
#FUNCTIONS 
def login():
    username = entry_username.get()
    password = entry_password.get()

    #read the json file and then store the extracted data to "login_data"
    with open("credentials.json","r") as read_login: 
        login_data = json.load(read_login)

    # Check if username and password are correct
    for every_login in login_data["login_details"]:
        if username == every_login["username"] and password == every_login["password"]:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            root.withdraw() #hide , withdraw() 
            open_next_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
  

def validate_input(text):
    return text.isdigit()

# Create the function to open the next window
def open_next_window():
    next_window = Toplevel()
    next_window.title("Next Window")
    next_window.geometry('400x500')
    next_window.configure(bg="lightgray")
    # Name Entry
    label_name = Label(next_window, text="Name:")
    label_name.grid(row=0, column=0, padx=5, pady=5)
    entry_name = Entry(next_window)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    # Course ComboBox
    label_course = Label(next_window, text="Course:")
    label_course.grid(row=1, column=0, padx=5, pady=5)
    courses = ["IT", "PA", "Entre", "SAIS", "Accounting"]
    course_var = StringVar()
    combobox_course = ttk.Combobox(next_window, textvariable=course_var, values=courses)
    combobox_course.grid(row=1, column=1, padx=5, pady=5)

    # Student ID Entry
    label_id = Label(next_window, text="Student ID:")
    label_id.grid(row=2, column=0, padx=5, pady=5)
    vcmd = (next_window.register(validate_input), '%P')
    entry_id = Entry(next_window, validate="key", validatecommand=vcmd)
    entry_id.grid(row=2, column=1, padx=5, pady=5)

    # Sex Radio Buttons
    label_sex = Label(next_window, text="Sex:")
    label_sex.grid(row=3, column=0, padx=5, pady=5)
    sex_var = StringVar()
    radio_male = Radiobutton(next_window, text="Male", variable=sex_var, value="Male")
    radio_male.grid(row=3, column=1, padx=5, pady=5)
    radio_female = Radiobutton(next_window, text="Female", variable=sex_var, value="Female")
    radio_female.grid(row=3, column=2, padx=5, pady=5)

    # Address Text widget
    label_address = Label(next_window, text="Address:")
    label_address.grid(row=4, column=0, padx=5, pady=5)
    text_address = Text(next_window, height=5, width=30)
    text_address.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    # Subjects Enrolled Checkbuttons
    label_subjects = Label(next_window, text="Subjects Enrolled:")
    label_subjects.grid(row=5, column=0, padx=5, pady=5)
    subjects = ["Math", "Science", "English", "History", "Art"]
    sbjEnrolled = []
    chk1 = StringVar() 
    chk2 = StringVar()
    chk3 = StringVar()
    chk4 = StringVar()
    chk5 = StringVar()

    check1 = Checkbutton(next_window,text="MATH", onvalue="MATH",offvalue="", variable=chk1)
    check2 = Checkbutton(next_window,text="MATH", onvalue="SCIENCE",offvalue="", variable=chk2)
    check3 = Checkbutton(next_window,text="MATH", onvalue="ENGLISH",offvalue="", variable=chk3)
    check4 = Checkbutton(next_window,text="MATH", onvalue="HISTORY",offvalue="", variable=chk4)
    check5 = Checkbutton(next_window,text="MATH", onvalue="ART",offvalue="", variable=chk5)

    #check Grids
    check1.grid(row= 6,column=1,columnspan=2)
    check2.grid(row= 7,column=1,columnspan=2)
    check3.grid(row= 8,column=1,columnspan=2)
    check4.grid(row= 9,column=1,columnspan=2)
    check5.grid(row= 10,column=1,columnspan=2)

    SaveBtn = Button(next_window, text="Save", width=7, height=3, command=lambda:save_data())
    SaveBtn.grid(row=10, column= 1,columnspan=2)
    
    def save_data():
        n = entry_name.get()
        c = combobox_course.get()
        id = entry_id.get()
        #radio button 
        s = sex_var.get()
        #text
    next_window.mainloop()
root.mainloop()