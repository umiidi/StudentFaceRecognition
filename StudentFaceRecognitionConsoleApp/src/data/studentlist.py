from src.data.students import Student

Students_id = []
Students = []

def name_request(imgname):
    try:
        id = int(imgname.split(".")[0])
        index = Students_id.index(id)
        return Students[index].name
    except:
        return "Unknown"

def add_user(id, name, surname, img):
    s = Student(id, name, surname, img)
    Students_id.append(s.id)
    Students.append(s)

def check_id(id):
    return Students_id.count(id)
