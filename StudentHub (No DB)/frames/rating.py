from tkinter import *
from tkinter import messagebox

def rating():
    from app import app
    from data.process import rayting_gpa

    rating_frame = Frame(app, bg="blue", width=800, height=600)
    list = rayting_gpa()
    header = Label(rating_frame, text="Rating", bg="blue", fg="white",  font="Constantia 35 bold")
    header.place(x = 350, y = 10)
    leaders = Label(rating_frame, bg="blue", width=90, height=41)
    leaders.place(x=131, y=70)
    if len(list) == 0:
        messagebox.showerror(title="Notification", message="There are no students in the base")
        return
    else:
        if len(list) >= 1:
            label1 = Label(leaders, text="1. ", bg="blue", fg="gold", font="Constantia 45 bold")
            label1.place(x=50, y=5)
            label1_name = Label(leaders, text=list[0].name + " " + list[0].surname + " (" + str(list[0].gpa) + ")", bg="blue", fg="white", font="Constantia 40 bold")
            label1_name.place(x=100, y=10)
        if len(list) >= 2:
            label2 = Label(leaders, text="2. ", bg="blue", fg="silver", font="Constantia 40 bold")
            label2.place(x=50, y=65)
            label2_name = Label(leaders, text=list[1].name + " " + list[1].surname + " (" + str(list[1].gpa) + ")", bg="blue", fg="white", font="Constantia 35 bold")
            label2_name.place(x=100, y=70)
        if len(list) >= 3:
            label3 = Label(leaders, text="3. ", bg="blue", fg="#CD7F32", font="Constantia 35 bold")
            label3.place(x=50, y=120)
            label3_name = Label(leaders, text=list[2].name + " " + list[2].surname + " (" + str(list[2].gpa) + ")", bg="blue", fg="white", font="Constantia 30 bold")
            label3_name.place(x=100, y=131)

    y = 185
    count = 4
    for i in list[3:10:]:
        Label(leaders, text=str(count) + ". ", bg="blue", fg="black", font="Constantia 25 bold").place(x=50, y=y)
        Label(leaders, text=list[2].name + " " + list[2].surname + " (" + str(list[2].gpa) + ")", bg="blue", fg="white", font="Constantia 23 bold").place(x=100, y=y)
        y+=50
        count+=1
    cancel = Button(rating_frame, text="CANCEL", font="Constantia", bg="white", width=7, height=1)
    cancel.configure(command=lambda: [rating_frame.destroy()])
    cancel.place(x=10, y=10)
    
    rating_frame.place(x=0, y=0)
