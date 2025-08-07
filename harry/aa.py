import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x500")
root.configure(bg="gray")

lb = Label(root,text=" Virtual Biodata ", background="Black",foreground="White",height=3,width=50)
lb.pack()

#Label
name_L = Label(root,text="Name: ", background="white")
age_L = Label(root,text="Age: ", background="white")
sex_E = Label(root,text="Sex")
course = Label(root,text="Course")

#L_place
name_L.place(x=20,y=75)
age_L.place(x=20,y=100)
sex_E.place(x=20,y=125)
course.place(x=20,y=185)




#Widgets

sex_V = tk.StringVar()
sub_V1 = StringVar()
sub_V2 = IntVar()
sub_V3 = IntVar()
sub_V4= IntVar()
name_E = Entry(root,width=30,highlightbackground="white")
age_E = Entry(root,width=30,highlightbackground="white")
sex_Em = tk.Radiobutton(root,text="MALE",value ="MALE",variable=sex_V)
sex_Ef = tk.Radiobutton(root,text="FEMALE",value ="FEMALE",variable=sex_V)
course_list = ["BSIT","BSIS","PA"] 
course_c = ttk.Combobox(root,values = course_list)
sub_L = Label(root,text="Subject Enrolled",bg="black",foreground="white")
sub_b1 = Checkbutton(root,text="Programming 2",offvalue=0,onvalue="Programming",variable=sub_V1)
sub_b2 = Checkbutton(root,text="Contemporary World",offvalue=0,onvalue=1,variable=sub_V2)
sub_b3 = Checkbutton(root,text="PE",offvalue=0,onvalue=1,variable=sub_V3)
sub_b4 = Checkbutton(root,text="Discrete Math",offvalue=0,onvalue=1,variable=sub_V4)
submit_b = Button(root,text="Submit",bg="black",fg="white",command=lambda:submit_info())

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

# rad = (sex_Em,sex_Ef)
def submit_info():
    n = name_E.get()
    a = age_E.get()
    s = sex_V.get()
    c= course_c.get()
    sub = []

    if sub_V1.get() == 1:
        sub.append("Programming 2")
    if sub_V2.get() == 1:
        sub.append("Contemporary World")
    if sub_V3.get() == 1:
        sub.append("PE")
    if sub_V4.get() == 1:
        sub.append("Discrete Math")
    message = f"\n\nName:{n}\nAge: {a}\nSex: {s}    \nCourse: {c} \nSubject Enrolled: {sub} "

    filename = 'saved_data.txt'
    with open(filename,'a') as collect:
        collect.write(message)
    messagebox.showinfo("Saved","Saved Data Succesfully")




root.mainloop()