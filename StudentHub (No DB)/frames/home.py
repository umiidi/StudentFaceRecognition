from tkinter import *
from frames.facerecognition import facerecognition
from frames.studentinfo import studentinfo
from frames.addstudent import addstudent
from frames.searchstudent import searchstudent
from frames.rating import rating
from frames.scorecalculator import scorecalculator
from data.process import random_student
def home():
    from app import app
    home_frame= Frame(app, bg="blue",width=800, height=600)
    home_frame.place(x=0, y=0)
    header = Label(home_frame, text="Student Hub",bg="blue", font="Constantia 30 bold", fg = "white")
    header.place(x=295, y=17)
    header2 = Label(home_frame, text="Creative Student App",bg="blue", font="Constantia 25", fg = "white")
    header2.place(x=260, y=61)
    menu = Label(home_frame, bg="red")
    menu.place(x=205,y=127)
    texts = ["Face Recognition",
             "Rating",
             "Search Student",
             "Add Student",
             "Random Student",
             "Score Calculator",
             "Exit"]
    commands = [lambda:[facerecognition()], 
                lambda:[rating()],
                lambda:[searchstudent()],
                lambda:[addstudent()],
                lambda:[studentinfo(random_student())],
                lambda:[scorecalculator()],
                lambda:[app.quit()]]
    for (text, command) in zip(texts, commands):
        Button(menu, text = text,font= "Constantia 20",fg = "black",command = command, width=25, height=1, borderwidth=5).pack(padx=1, pady=1)