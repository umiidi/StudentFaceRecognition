from src.data.students import Student
from src.data.studentlist import add_user

filename = 'src/data/StudentInformation.txt'


def start_file_process():
    lines = read_file()
    for line in lines:
        if line == "\n": continue
        info = line.split("|")
        id = info[0]
        name = info[1]
        surname = info[2]
        img = info[3]
        add_user(id, name, surname, img)

def read_file():
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except:
        exit("No Read File")

def write_to_file(line):
    with open(filename, 'a') as f:
        f.write(line)
