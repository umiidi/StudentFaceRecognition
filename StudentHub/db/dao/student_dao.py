from db.dao.abstract_dao import AbstractDao
from db.entity.groups import Group
from db.entity.student import Student

class StudentDao(AbstractDao):
    def get_all_students(self):
        connection = self.connect()
        cursor = connection.cursor()
        query = "SELECT *, g.name as group_name \
                FROM student AS s \
                LEFT JOIN `group` AS g ON g.id= s.group_id"
        cursor.execute(query)
        records = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        students = []
        for record in records:
            id = record[field_names.index('id')]
            name = record[field_names.index('name')]
            surname = record[field_names.index('surname')]
            gender = record[field_names.index('gender')]
            email = record[field_names.index('email')]
            phone = record[field_names.index('phone')]
            image = record[field_names.index('image')]
            group_id = record[field_names.index('group_id')]
            group_name = record[field_names.index('group_name')]
            students.append(Student(id=id, name=name, surname=surname, gender=gender, email=email, phone=phone, Group=Group(group_id, group_name),image=image))
        cursor.close()
        connection.close()
        return students

    def get_student_by_id(self, student_id):
        connection = self.connect()
        cursor = connection.cursor()
        query = "SELECT s.*, g.name AS group_name " \
                "FROM student AS s " \
                "LEFT JOIN `group` AS g ON g.id = s.group_id " \
                "WHERE s.id = %s"
        cursor.execute(query, (student_id, ))
        student = cursor.fetchone()
        cursor.close()
        connection.close()
        if student:
            id, name, surname, gender, email, phone, image, group_id, group_name = student
            return Student(id, name, surname, gender, email, phone, image, Group=Group(group_id, group_name))
        else:
            return None

    def get_student_by_face_record_id(self, face_record_id):
        connection = self.connect()
        cursor = connection.cursor()
        query = "SELECT s.*, g.name as group_name " \
                "FROM student AS s " \
                "LEFT JOIN `group` as g on g.id = s.group_id " \
                "LEFT JOIN face_record AS fr ON fr.student_id = s.id " \
                "WHERE fr.id = %s"
        cursor.execute(query, (face_record_id, ))
        student = cursor.fetchone()
        cursor.close()
        connection.close()
        if student:
            id, name, surname, gender, email, phone, image, group_id, group_name = student
            return Student(id, name, surname, gender, email, phone, image, Group=Group(group_id, group_name))
        else:
            return None

    def add_student(self, student):
        connection = self.connect()
        cursor = connection.cursor()
        query = "INSERT INTO student \
                (name, surname, gender, email, phone, image, group_id) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (student.name, student.surname, student.gender, student.email, student.phone, student.image, student.Group.id))
        connection.commit()
        cursor.close()
        connection.close()
    
    def update_student(self, student):
        connection = self.connect()
        cursor = connection.cursor()
        query = "UPDATE student SET \
                name = %s, surname = %s, gender = %s,  email = %s, phone = %s, image = %s, group_id = %s \
                WHERE id = %s"
        cursor.execute(query, (student.name, student.surname, student.gender, student.email, student.phone, student.image, student.Group.id, student.id))
        connection.commit()
        cursor.close()
        connection.close()

    def remove_student(self, student_id):
        connection = self.connect()
        cursor = connection.cursor()
        query = "DELETE FROM student WHERE id = %s"
        cursor.execute(query, (student_id,))
        connection.commit()
        cursor.close()
        connection.close()