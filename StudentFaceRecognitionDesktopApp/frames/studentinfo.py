from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
def studentinfo(s):
    if s == None:
        messagebox.showerror(title="Notification", message="There are no students in the base")
        return
    from app import app
    student_info_frame = Frame(app, bg="Blue", width=800, height=600)
    header = Label(student_info_frame,text="About Student", fg="white",background="blue",font=("Constantia 25 bold"))
    header.place(x = 300, y=20)

    Label(student_info_frame,text="Name", font="Constantia 15 bold", fg="white", background="blue").place(x=50, y=120)
    Label(student_info_frame,text=s.name, font="Arial 15", bg="white", fg = "black", width=20, border=3, relief="solid").place(x=50, y=150)

    Label(student_info_frame,text="Surname", font="Constantia 15 bold", fg="white",background="blue").place(x=300, y=120)
    Label(student_info_frame,text=s.surname, font="Arial 15", bg="white", fg = "black", width=20, border=3, relief="solid").place(x=300, y=150)

    Label(student_info_frame,text="Father name", font="Constantia 15 bold", fg="white", background="blue").place(x=50, y=200)
    Label(student_info_frame,text=s.fathername, font="Arial 15", bg="white", fg = "black", width=20, border=3, relief="solid").place(x=50, y=230)

    Label(student_info_frame,text="Birth date", font="Constantia 15 bold", fg="white", background="blue").place(x=300, y=200)
    Label(student_info_frame,text=s.birthdate, font="Arial 15", bg="white", fg = "black", width=11, border=3, relief="solid").place(x=300, y=230)

    Label(student_info_frame,text="Gender", font="Constantia 15 bold", fg="white", background="blue").place(x=300, y=280)
    Label(student_info_frame,text=s.gender, font="Arial 15", bg="white", fg = "black", width=7, border=3, relief="solid").place(x=300, y=310)
    
    Label(student_info_frame,text="GPA", font="Constantia 15 bold", fg="white", background="blue").place(x=420, y=280)
    Label(student_info_frame,text=s.gpa, font="Arial 15", bg="white", fg = "black", width=5, border=3, relief="solid").place(x=420, y=310)

    Label(student_info_frame,text="Group", font="Constantia 15 bold", fg="white", background="blue").place(x=50, y=280)
    Label(student_info_frame,text=s.group, font="Arial 15", bg="white", fg = "black", width=20, border=3, relief="solid").place(x=50, y=310)

    Label(student_info_frame,text="Contacts", font="Constantia 20 bold", fg="white", background="blue").place(x=50, y=410)

    Label(student_info_frame,text="Phone", font="Constantia 15 bold", fg="white", background="blue").place(x=50, y=460)
    Label(student_info_frame,text=s.phone, font="Arial 15", bg="white", fg = "black", width=20, border=3, relief="solid").place(x=150, y=460)

    Label(student_info_frame,text="Mail", font="Constantia 15 bold", fg="white", background="blue").place(x=50, y=500)
    Label(student_info_frame,text=s.mail, font="Arial 15", bg="white", fg = "black", width=27, border=3, relief="solid").place(x=150, y=500)

    img = ImageTk.PhotoImage(Image.open(str("data/imgdata/"+ s.image)).resize((150, 200)))
    image = Label(student_info_frame, image=img, bg="white", borderwidth=6, relief="solid")
    image.image = img
    image.place(x = 580, y=130)

    cancel = Button(student_info_frame, text = "CANCEL", font = "Constantia", bg = "white", width = 7, height= 1)
    cancel.configure(command= lambda: [student_info_frame.destroy()])              
    cancel.place(x=10,y=10)
    student_info_frame.place(x=0, y=0)