import random

from src.data.fileprocess import write_to_file
from src.data.studentlist import check_id, add_user


def registration():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    id = id_generator()
    img = f"{id}.png"
    add_user(id, name, surname, img)
    write_to_file(str(id) + '|' + name + '|' + surname + '|' + img+ '\n')
    print("Registration Successfully!")
    print("Please, upload your image it to the 'imgdata' folder with this name: ", img)

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

registration()
