from db.entity.groups import Group 

class Student:

    def __init__(self, id, name, surname, gender, phone, email, image, Group) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.gender = gender
        self.phone = phone
        self.email = email
        self.image = image
        self.Group = Group
    
    def __str__(self) -> str:
        return f"Student{{id: {self.id}, name: {self.name}, surname: {self.surname}, gender: {self.gender}, phone: {self.phone}, email: {self.email}, image: {self.image}, Group: {self.Group}}}"
