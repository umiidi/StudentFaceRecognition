import pickle

class Student:
    def __init__(self, id, name, surname, fathername, birthdate, gender, gpa, group, phone, mail, image):
        self.id = id
        self.name = name
        self.surname = surname
        self.fathername = fathername
        self.group = group
        self.birthdate = birthdate
        self.gender = gender
        self.gpa = gpa
        self.phone = phone
        self.mail = mail
        self.image = image

class Config:
    def __init__(self, studentid = [], studentlist = []):
        self.studentid = studentid
        self.studentlist = studentlist

config = None

def getconfig():
    global config
    if config == None:
        config = Config()
    return config

def add(id, student):
    getconfig().studentid.append(id)
    getconfig().studentlist.append(student)
    update()

def remove(index):
    getconfig().studentid.pop(index)
    getconfig().studentlist.pop(index)
    update()

def update():
    update_config()

def update_config():
    with open("data/data.obj", "wb") as file:
        pickle.dump(getconfig(), file)

def read_config():
    global config
    try:
        with open("data/data.obj", "rb") as file:
            config = pickle.load(file)
    except: config = Config()