import cv2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from data.recognition import count_face, framesrecognition

def facerecognition():
    from app import app
    from frames.studentinfo import studentinfo
    face_recognition_frame = Frame(app, bg="blue", width = 800, height= 600)
    face_recognition_frame.place(x=0, y=0)
    facelabel = Label(face_recognition_frame, bg="gray")
    facelabel.place(x=10, y=10)
    video_capture = cv2.VideoCapture(0)
    namelabel = Label(face_recognition_frame, text = "Loading", font="Constantia 20 bold", width=8, height=1)
    namelabel.place(x=348, y=527)
    time = 0
    frames = []
    student = None
    def show_frame():
        nonlocal time, frames, student, video_capture
        ret, frame = video_capture.read()
        img  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img  = Image.fromarray(img).resize((775, 570))
        imgtk = ImageTk.PhotoImage(image = img)
        facelabel.imgtk = imgtk
        facelabel.configure(image=imgtk)
        count = count_face(frame)
        if count!=1:
            if count == 0: namelabel.configure(text= "No face")
            else: text = namelabel.configure(text= "Many faces")
            frames.clear()
            time = 0
        else:
            if time == 0:
                namelabel.configure(text= "Loading")
            elif time == 200:
                namelabel.configure(text= "Loading.")
                frames.append(frame)
            elif time == 400:
                namelabel.configure(text= "Loading..")
                frames.append(frame)
            elif time == 600:
                namelabel.configure(text= "Loading...")
                frames.append(frame)
            elif time == 650:
                student = framesrecognition(frames)
                if student != None:
                    if messagebox.askyesno(title="Student App", message=str("Name: ") + student.name + str("\nSurname: ") + student.surname + str("\nWant to see more information?")):
                        video_capture.release()
                        face_recognition_frame.destroy()
                        studentinfo(student)
                        return
                    else: time = 0
                else: 
                    messagebox.showerror(title="Student App", message="The student's face was not found in the database!")
                    time = 0
            time+=10
        facelabel.after(10, show_frame)
    
    cancel = Button(face_recognition_frame, text = "CANCEL", font = "Constantia", bg = "white", width = 10, height= 1)
    cancel.configure(command= lambda: [video_capture.release(), face_recognition_frame.destroy()])
    cancel.place(x=355,y=565)

    show_frame()