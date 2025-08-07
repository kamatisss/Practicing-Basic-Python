from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel
import json
import os

root = Tk()
root.configure(bg="white")
root.title("Login")

def login_fun():
    username = e_name.get()
    password = e_pass.get()

    #read the json file and then store the extracted data to "login_data"
    with open("Login.json","r") as r_login: 
        login_data = json.load(r_login)

    # Check if username and password are correct
    for every_login in login_data["login_details"]:
        if username == every_login["username"] and password == every_login["password"]:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            root.withdraw() #hide , withdraw() 
            biodata_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

l_name = Label(root,text="Username")
l_pass = Label(root,text="Password")
l_name.grid(row=0,column=0)
l_pass.grid(row=1,column=0)
e_name = Entry(root)
e_pass = Entry(root)
e_name.grid(row=0,column=1)
e_pass.grid(row=1,column=1)

log_B = Button(root,text="Login",command=lambda:login_fun())
log_B.grid(row=2,column=1)


  

def validate_input(text):
    return text.isdigit()

def biodata_window():
    roota = Toplevel()
    roota.geometry("300x500")
    roota.configure(bg="gray")

    def submit_info():
        n = name_E.get()
        a = age_E.get()
        s = sex_V.get()
        c= course_c.get()
        sub = []
    
        new_bio_info = {
            "name":n, 
            "sex":s,
            "age": a, 
            "course":c,
            "Subjects":sub
        }
        if sub_V1.get() == 1:
            sub.append("Programming 2")
        if sub_V2.get() == 1:
            sub.append("Contemporary World")
        if sub_V3.get() == 1:
            sub.append("PE")
        if sub_V4.get() == 1:
            sub.append("Discrete Math")

      
        file = 'amanteser.json'
        if os.path.exists(file): 
            with open(file, 'r') as r_file:
                bio_info = json.load(r_file)
                # print(student_info)

        else:
            bio_info = {"ana_information":[]}
            with open(file, 'w') as c_file:
                json.dump(bio_info, c_file, indent=3)

        bio_info["ana_information"].append(new_bio_info)
        with open(file, 'w') as update_file:
            json.dump(bio_info,update_file, indent=4 )
        messagebox.showinfo("BIODATA INFO", "DATA SAVED SUCCESSFULLY")



    lb = Label(root,text=" Virtual Biodata ", background="Black",foreground="White",height=3,width=50)
    lb.pack()

    #Label
    name_L = Label(roota,text="Name: ", background="white")
    age_L = Label(roota,text="Age: ", background="white")
    sex_E = Label(roota,text="Sex")
    course = Label(roota,text="Course")

    #L_place
    name_L.place(x=20,y=75)
    age_L.place(x=20,y=100)
    sex_E.place(x=20,y=125)
    course.place(x=20,y=185)




    #Widgets

    sex_V = StringVar()
    sub_V1 = IntVar()
    sub_V2 = IntVar()
    sub_V3 = IntVar()
    sub_V4= IntVar()
    name_E = Entry(roota,width=30,highlightbackground="white")
    age_E = Entry(roota,width=30,highlightbackground="white")
    sex_Em = Radiobutton(roota,text="MALE",variable=sex_V,value ="MALE")
    sex_Ef = Radiobutton(roota,text="FEMALE",variable=sex_V,value ="FEMALE")
    course_list = ["BSIT","BSIS","PA"] 
    course_c = ttk.Combobox(roota,values = course_list)
    sub_L = Label(roota,text="Subject Enrolled",bg="black",foreground="white")
    sub_b1 = Checkbutton(roota,text="Programming 2",offvalue=0,onvalue="Programming",variable=sub_V1)
    sub_b2 = Checkbutton(roota,text="Contemporary World",offvalue=0,onvalue=1,variable=sub_V2)
    sub_b3 = Checkbutton(roota,text="PE",offvalue=0,onvalue=1,variable=sub_V3)
    sub_b4 = Checkbutton(roota,text="Discrete Math",offvalue=0,onvalue=1,variable=sub_V4)
    submit_b = Button(roota,text="Submit",bg="black",fg="white",command=lambda:submit_info())

    #E_place
    name_E.place(x=75,y=75)
    age_E.place(x=75,y=100)
    sex_Em.place(x=75,y=125)
    sex_Ef.place(x=75,y=155)
    course_c.place(x=75,y=185)
    sub_L.place(x=75,y=205)
    sub_b1.place(x=75,y=230)
    sub_b2.place(x=75,y=255)
    sub_b3.place(x=75,y=280)
    sub_b4.place(x=75,y=305)
    submit_b.place(x=75,y=330)





    roota.mainloop()
root.mainloop()