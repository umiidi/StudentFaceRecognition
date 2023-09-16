from tkinter import *
from PIL import Image, ImageTk
from data.process import get_students

def searchstudent():
    from app import app
    from frames.studentinfo import studentinfo
    from frames.editstudent import editstudent

    searchstudentframe = Frame(app, bg="blue", width=800, height=600)
    searchstudentframe.pack(fill=BOTH, expand=True)


    header1 = Label(searchstudentframe, bg="blue")
    searchtxt = Entry(header1, font=("times new roman", 20), bg = "white", fg = "black", width=27)
    searchtxt.pack(padx=200, pady=27)
    searchbutton = Button(header1, text = "SEARCH", font = "Constantia", bg = "white", width = 10, height= 1)
    searchbutton.configure(command= lambda: [showresult(searchtxt.get())])              
    searchbutton.place(x=600,y=25)
    cancel = Button(header1, text = "CANCEL", font = "Constantia", bg = "white", width = 7, height= 1)
    cancel.configure(command= lambda: [searchstudentframe.destroy()])              
    cancel.place(x=10,y=10)
    header1.pack()

    header2 = Label(searchstudentframe, bg="blue")
    Label(header2, text="Image", font= "Constantia 20 bold", bg="gray", border=3, relief="solid").grid(row=0, column=0)
    Label(header2, text="       Name|Surname       ", font= "Constantia 20 bold", bg="gray", border=3, relief="solid").grid(row=0, column=1)
    Label(header2, text="Info/Edit", font= "Constantia 20 bold", bg="gray", border=3, relief="solid").grid(row=0, column=2)
    header2.pack()
    
    canvas = Canvas(searchstudentframe, bg="blue", borderwidth=-3)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(searchstudentframe, orient="vertical", command=canvas.yview, bg="red")
    scrollbar.pack(side="right", fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    result = Frame(canvas)
    
    def showresult(searchtxt = None):
        nonlocal result
        result.destroy()
        list = get_students(searchtxt)
        result = Frame(canvas, bg="blue", width=800, height=len(list)*65)
        canvas.create_window((0, 0), window=result, anchor='nw')
        y = 0
        count = 0
        for i in list:
            def info(n = i):
                studentinfo(n)
            def edit(n = i):
                editstudent(n)
            imgname = i.image
            img = ImageTk.PhotoImage(Image.open("data/imgdata/" + str(imgname)).resize((80,70)))
            image = Label(result, image=img, bg="gray", border=3, relief="solid", width=80, height=60)
            image.image = img
            image.place(x=150, y=y)
            Label(result, text= str(i.name + " " + i.surname + "\n" + i.fathername), font="Constantia 18 bold", bg="gray", border=3, relief="solid", width=19, height=2).place(x = 235, y=y)
            Button(result, text="View", font="Constantia 13 bold", bg="gray", border=3, relief="solid", command = info, width=11, height=1).place(x = 527, y=y)
            Button(result, text="Edit", font="Constantia 12 bold", bg="gray", border=3, relief="solid", command = edit, width=11, height=1).place(x = 527, y=y+31)
            count+=1
            y+= 65
        result.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
    showresult()

    