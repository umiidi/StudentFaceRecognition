from data.config import Student, getconfig, add, remove, update
import random
import shutil
import os

def add_student(name, surname, fathername, birthdate, gender, gpa, group, phone, mail, image):
    id = id_generator()
    newimage = str(id) + ".png"
    shutil.copyfile(image, str("data/imgdata/") + newimage)
    student = Student(id=id, name=name, surname=surname, fathername=fathername, birthdate=birthdate, gender=gender, gpa=gpa, group=group, phone=phone, mail=mail, image=newimage)
    add(id, student)

def remove_student(s):
    os.remove("data/imgdata/" + str(s.image))
    remove(getconfig().studentid.index(s.id))

def update_information(id, name, surname, fathername, birthdate, gender, gpa, group, phone, mail, image):
    s = get_student(id)
    try:
        newimage = str(id) + ".png"
        shutil.copyfile(image, str("data/imgdata/") + newimage)
        s.image = newimage
    except: pass
    s.name = name
    s.surname = surname
    s.fathername = fathername
    s.birthdate = birthdate
    s.gender = gender
    s.gpa = gpa
    s.group = group
    s.phone = phone
    s.mail = mail
    update()

def get_all_students():
    return getconfig().studentlist

def get_students(searchtxt):
    if searchtxt == None or searchtxt == "":
        list = get_all_students()
        # list.append(list[0])
        # list.append(list[1])
        # list.append(list[2])
        return get_all_students()
    else:
        resultlist = []
        for i in get_all_students():
            if searchtxt in i.name or searchtxt in i.surname:
                resultlist.append(i)
        return resultlist

def get_student(id):
    if check_id(id):
        return getconfig().studentlist[getconfig().studentid.index(id)]
    else: return None

def name_request(id):
    try:
        return getconfig().studentlist[getconfig().studentid.index(id)].name
    except:
        return "Unknown"

def check_id(id):
    if getconfig().studentid.count(id) == 0: return False
    else: return True

def random_id_generator():
    id = 0
    for i in range(4):
        temp = random.randrange(1, 10)
        id = id * 10 + temp
    else:
        return id

def id_generator():
    id = random_id_generator()
    while check_id(id):
        id = random_id_generator()
    else:
        return id
    
def random_student():
    lenn = len(getconfig().studentlist)
    if lenn == 0: return None
    index = random.randrange(0, lenn)
    return getconfig().studentlist[index]

def rayting_gpa():
    students = list(get_all_students())
    n = len(students)
    for i in range(n):
        for j in range(n-i-1):
            if students[j].gpa < students[j+1].gpa:
                students[j], students[j+1] = students[j+1], students[j]
    return students

