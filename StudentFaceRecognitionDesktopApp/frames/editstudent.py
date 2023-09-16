from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import filedialog, messagebox
from data.process import update_information, remove_student

def editstudent(s):
    from app import app
    editstudent_frame = Frame(app, bg="Blue",width=800, height=600)
    Label(editstudent_frame,  text="UPDATE", font="Constantia 30 bold" ,fg="white", bg="blue").place(x=300, y=10)

    Label(editstudent_frame, text="Name", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=30, y=120)
    name = Entry(editstudent_frame, font=("times new roman", 15), bg = "white", fg = "black")
    name.insert(0, s.name)
    name.place(x=30, y=150)

    Label(editstudent_frame, text="Surname", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=280, y=120)
    surname = Entry(editstudent_frame, font=("times new roman", 15), bg = "white", fg = "black")
    surname.insert(0, s.surname)
    surname.place(x=280, y=150)

    Label(editstudent_frame, text="Father name", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=30, y=200)
    fathername = Entry(editstudent_frame, font=("times new roman", 15), bg = "white", fg = "black")
    fathername.insert(0, s.fathername)
    fathername.place(x=30, y=230)

    Label(editstudent_frame, text="Date of Birth", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=280, y=200)
    selected = str(s.birthdate).split("/")
    birthdate = DateEntry(editstudent_frame, date_pattern = "DD/MM/YYYY", day = int(selected[0]), month = int(selected[1]), year = int(selected[2]))
    birthdate.place(x=280, y=232)
    
    Label(editstudent_frame, text="Gender", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=280, y=280)
    options = [s.gender, "Male", "Female"]
    gender = StringVar(editstudent_frame)
    gender.set(options[0])
    ttk.OptionMenu(editstudent_frame, gender, *options).place(x=280, y=310)

    def validate_input(new_value):
        return new_value.isdigit() or new_value == ""
    validate_command = editstudent_frame.register(validate_input)
    Label(editstudent_frame, text="GPA", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=405, y=280)
    gpa =  Spinbox(editstudent_frame, from_=1, to=100, increment=1, validate="key", validatecommand=(validate_command, "%P"), width=10)
    gpa.delete(0, END)
    gpa.insert(0, s.gpa)
    gpa.place(x=405, y=312)

    Label(editstudent_frame, text="Group", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=30, y=280)
    group = Entry(editstudent_frame, font=("times new roman", 15), bg = "white", fg = "black")
    group.insert(0, s.group)
    group.place(x=30, y=310)

    Label(editstudent_frame, text="Phone", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=30, y=360)
    phone = Entry(editstudent_frame, font=("times new roman", 15), bg = "white", fg = "black")
    phone.insert(0, s.phone)
    phone.place(x=30, y=390)

    Label(editstudent_frame, text="Email Address", font=("times new roman",15, "bold"), bg = "blue", fg = "black").place(x=280, y=360)
    mail = Entry(editstudent_frame, font=("times new roman", 15), bg = "white", fg = "black", width=27)
    mail.insert(0, s.mail)
    mail.place(x=280, y=390)

    img = ImageTk.PhotoImage(Image.open("data/imgdata/" + s.image).resize((200,250)))
    image = Label(editstudent_frame, image=img, bg="white", borderwidth=6, relief="solid")
    image.image = img
    image.place(x = 580 , y=130)

    upload = Button(editstudent_frame, text = "UPLOAD", font = "Constantia", bg = "white", width = 10, height= 1)
    upload.configure(command= lambda: [image_upload()])              
    upload.place(x=627,y=400)
    imgname = s.image

    def image_upload():
        nonlocal imgname
        file_types = [("PNG", "*.png"), ("JPG", "*.jpg"), ("Bitmap", "*.bmp")]
        inputimg = filedialog.askopenfilename(filetypes=file_types)
        if inputimg == "": return
        else: imgname = inputimg
        try:
            newimg = ImageTk.PhotoImage(Image.open(imgname).resize((200,250)))
            image['image'] = newimg
            image.image = newimg
        except: pass

    update = Button(editstudent_frame, text = "UPDATE", font = "Constantia 20 bold", bg = "white", fg="green", width = 7, height= 1)
    update.configure(command= lambda: [update()])              
    update.place(x=270,y=500)

    def removestudent():
        if messagebox.askyesno(title="Notification", message="Are you sure?"):
            remove_student(s=s)
            messagebox.showinfo(title="Notification", message="Successfully Deleted")
            cancel.invoke()
        else: pass

    delete = Button(editstudent_frame, text = "Remove", font = "Constantia 20 bold", bg = "white", fg="green", width = 7, height= 1)
    delete.configure(command= lambda: [removestudent()])              
    delete.place(x=400,y=500)

    def update():
        from data.recognition import check_face
        #TESTLER APARILMALIDIR
        if not check_face(imgname):
                messagebox.showerror(title="Notification", message="The picture you upload cannot be used as a profile picture")
        elif gender.get() == "Choose":
            messagebox.showerror(title="Notification", message="Please select a gender")
        elif int(gpa.get()) < 1 or int(gpa.get()) > 100:
            messagebox.showerror(title="Notification", message="GPA was not entered correctly")
        else:
            if messagebox.askyesno(title="Notification", message="Are you sure?"):
                update_information(id=s.id, name = name.get(), surname = surname.get(), fathername=fathername.get(), 
                    birthdate=birthdate.get(), gender=gender.get(), gpa=int(gpa.get()), group=group.get(), phone = phone.get(), 
                    mail= mail.get(), image=imgname)
                messagebox.showinfo(title="Notification", message="Successfully Updated")
                cancel.invoke()
        
    cancel = Button(editstudent_frame, text = "CANCEL", font = "Constantia", bg = "white", width = 7, height= 1)
    cancel.configure(command= lambda: [editstudent_frame.destroy()])              
    cancel.place(x=10,y=10)
    editstudent_frame.place(x=0, y=0)
