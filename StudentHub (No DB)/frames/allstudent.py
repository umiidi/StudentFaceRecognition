from tkinter import *
from PIL import Image, ImageTk
from data.process import get_students

def allstudents():
    from app import app
    from frames.studentinfo import studentinfo
    searchstudentframe = Frame(app, bg="Blue",width=800, height=600)
    searchstudentframe.place(x=0, y=0)

    searchtxt = Entry(searchstudentframe, font=("times new roman", 20), bg = "white", fg = "black", width=27)
    searchtxt.place(x=200, y=30)

    resultlabel = Label()

    searchbutton = Button(searchstudentframe, text = "SEARCH", font = "Constantia", bg = "white", width = 10, height= 1)
    searchbutton.configure(command= lambda: [resultlabel.destroy(), showresult(searchtxt.get())])              
    searchbutton.place(x=600,y=31)
    def showresult(searchtxt = None):
        nonlocal resultlabel
        resultlabel = Label(searchstudentframe, bg = "gray", width=1000, height=30, border=3, relief="solid")
        list = get_students(searchtxt)
        y = 50
        count = 1
        Label(resultlabel, text="   Image   ", font= "Constantia 20 bold", bg="gray", border=3, relief="solid").grid(row=0, column=1)
        Label(resultlabel, text="        Name|Surname        ", font= "Constantia 20 bold", bg="gray", border=3, relief="solid").grid(row=0, column=2)
        Label(resultlabel, text=" Info ", font= "Constantia 20 bold", bg="gray", border=3,relief="solid").grid(row=0, column=3)
        Label(resultlabel, text=" Edit ", font= "Constantia 20 bold", bg="gray", border=3, relief="solid").grid(row=0, column=4)
        for n in range(1):
            for i in list[0:5]:
                def info(n = i):
                    studentinfo(n)

                imgname = i.image
                img = ImageTk.PhotoImage(Image.open("data/imgdata/" + str(imgname)).resize((70,70)))
                image = Label(resultlabel, image=img, bg="gray", border=3, relief="solid")
                image.image = img
                image.grid(row=count, column=1, sticky = "nsew")
                Label(resultlabel,text= str(i.name + " " + i.surname), font="Constantia 20 bold", bg="gray", border=3, relief="solid").grid(row=count, column=2, sticky = "nsew")
                Button(resultlabel, text="View", font="Constantia 15 bold", bg="gray", border=3, relief="solid", command = info).grid(row=count, column=3, sticky = "nsew")
                Button(resultlabel, text="Edit", font="Constantia 15 bold", bg="gray", border=3, relief="solid").grid(row=count, column=4, sticky = "nsew")
                count+=1
                y+= 60
            resultlabel.place(x = 120, y = 100)
    showresult()

    cancel = Button(searchstudentframe, text = "CANCEL", font = "Constantia", bg = "white", width = 7, height= 1)
    cancel.configure(command= lambda: [searchstudentframe.destroy()])              
    cancel.place(x=10,y=10)