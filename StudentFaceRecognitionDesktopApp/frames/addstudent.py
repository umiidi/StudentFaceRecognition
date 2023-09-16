from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import filedialog, messagebox
from data.process import add_student

def addstudent():
    from app import app
    add_student_frame = Frame(app, bg="Blue",width=800, height=600)
    Label(add_student_frame,  text="REGISTRATION", font="Constantia 30 bold" ,fg="white", bg="blue").place(x=300, y=10)

    Label(add_student_frame, text="Name", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=30, y=120)
    name = Entry(add_student_frame, font=("times new roman", 15), bg = "white", fg = "black")
    name.place(x=30, y=150)

    Label(add_student_frame, text="Surname", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=280, y=120)
    surname = Entry(add_student_frame, font=("times new roman", 15), bg = "white", fg = "black")
    surname.place(x=280, y=150)

    Label(add_student_frame, text="Father name", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=30, y=200)
    fathername = Entry(add_student_frame, font=("times new roman", 15), bg = "white", fg = "black")
    fathername.place(x=30, y=230)

    Label(add_student_frame, text="Date of Birth", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=280, y=200)
    birthdate = DateEntry(add_student_frame, date_pattern = "DD/MM/YYYY")
    birthdate.place(x=280, y=232)
    
    Label(add_student_frame, text="Gender", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=280, y=280)
    options = ["Choose", "Male", "Female"]
    gender = StringVar(add_student_frame)
    gender.set(options[0])
    ttk.OptionMenu(add_student_frame, gender, *options).place(x=280, y=310)

    def validate_input(new_value):
        return new_value.isdigit() or new_value == ""
    validate_command = add_student_frame.register(validate_input)
    Label(add_student_frame, text="GPA", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=405, y=280)
    gpa =  Spinbox(add_student_frame, from_=1, to=100, increment=1, validate="key", validatecommand=(validate_command, "%P"), width=10)
    gpa.place(x=405, y=312)

    Label(add_student_frame, text="Group", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=30, y=280)
    group = Entry(add_student_frame, font=("times new roman", 15), bg = "white", fg = "black")
    group.place(x=30, y=310)

    Label(add_student_frame, text="Phone", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=30, y=360)
    phone = Entry(add_student_frame, font=("times new roman", 15), bg = "white", fg = "black")
    phone.place(x=30, y=390)

    Label(add_student_frame, text="Email Address", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=280, y=360)
    mail = Entry(add_student_frame, font=("times new roman", 15), bg = "white", fg = "black", width=27)
    mail.place(x=280, y=390)

    img = ImageTk.PhotoImage(Image.open("unknown.jpg").resize((200,250)))
    image = Label(add_student_frame, image=img, bg="white", borderwidth=6, relief="solid")
    image.image = img
    image.place(x = 580 , y=130)

    upload = Button(add_student_frame, text = "UPLOAD", font = "Constantia", bg = "white", width = 10, height= 1)
    upload.configure(command= lambda: [image_upload()])              
    upload.place(x=635,y=400)
    imgname = "unknown.jpg"

    def image_upload():
        nonlocal imgname
        file_types = [("PNG", "*.png"), ("JPG", "*.jpg"), ("Bitmap", "*.bmp")]
        imgname =  filedialog.askopenfilename(filetypes=file_types)
        try:
            newimg = ImageTk.PhotoImage(Image.open(imgname).resize((200,250)))
            image['image'] = newimg
            image.image = newimg
        except: pass

    submit = Button(add_student_frame, text = "SUBMIT", font = "Constantia 20 bold", bg = "white", fg="green", width = 7, height= 1)
    submit.configure(command= lambda: [submit()])              
    submit.place(x=300,y=500)	

    def submit():
        from data.recognition import check_face
        #TESTLER APARILMALIDIR
        if not check_face(imgname):
            messagebox.showerror(title="Notification", message="The picture you upload cannot be used as a profile picture")
        elif gender.get() == "Choose":
            messagebox.showerror(title="Notification", message="Please select a gender")
        elif len(str(gpa.get())) == 0 or int(gpa.get()) < 1 or int(gpa.get()) > 100:
            messagebox.showerror(title="Notification", message="GPA was not entered correctly")
        else:
            if messagebox.askyesno(title="Notification", message="Are you sure?"):
                add_student(name = name.get(), surname = surname.get(), fathername=fathername.get(), 
                    birthdate=birthdate.get(), gender=gender.get(), gpa=int(gpa.get()), group=group.get(), phone = phone.get(), 
                    mail= mail.get(), image=imgname)
                messagebox.showinfo(title="Notification", message="REGISTRATION SUCCESSFULLY")
                cancel.invoke()

    cancel = Button(add_student_frame, text = "CANCEL", font = "Constantia", bg = "white", width = 7, height= 1)
    cancel.configure(command= lambda: [add_student_frame.destroy()])              
    cancel.place(x=10,y=10)
    add_student_frame.place(x=0, y=0)
