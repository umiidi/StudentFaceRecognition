import tkinter
from frames.home import home

app = tkinter.Tk()

def start_app():
    create_app()
    home()
    app.mainloop()

def create_app():
    app.title("Student Hub")
    app.geometry("800x600")
    app.minsize(800,600)
    app.maxsize(800,600)