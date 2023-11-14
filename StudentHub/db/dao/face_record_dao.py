from db.dao.abstract_dao import AbstractDao
from db.entity.face_record import FaceRecord

class FaceRecordDao(AbstractDao):
    def get_all_face_records(self):
        connection = self.connect()
        cursor = connection.cursor()
        query = "SELECT * FROM face_record"
        cursor.execute(query)
        student_face_records = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        student_faces = []
        for group in student_face_records:
            id = group[field_names.index('id')]
            student_id = group[field_names.index('student_id')]
            face_encoding = group[field_names.index('face_encoding')]
            image_url = group[field_names.index('image_url')]
            student_faces.append(FaceRecord(id=id, student_id=student_id ,face_encoding=face_encoding, image_url=image_url))
        cursor.close()
        connection.close()
        return student_faces

    def get_face_record_by_id(self, face_record_id):
        connection = self.connect()
        cursor = connection.cursor()
        query = "SELECT fr.id, fr.student_id, fr.face_encoding, fr.image_url FROM face_record AS fr WHERE id = %s"
        cursor.execute(query, (face_record_id,))
        face_record = cursor.fetchone()
        cursor.close()
        connection.close()
        if face_record:
            id, student_id, face_encoding, image_url = face_record
            return FaceRecord(id, student_id, face_encoding, image_url)
        else:
            return None

    def add_face_record(self, face_record):
        connection = self.connect()
        cursor = connection.cursor()
        query = "INSERT INTO face_record (student_id, face_encoding, image_url) VALUES (%s, %s, %s)"
        cursor.execute(query, (face_record.student_id, face_record.face_encoding, face_record.image_url))
        connection.commit()
        cursor.close()
        connection.close()
    
    def update_face_record(self, face_record):
        connection = self.connect()
        cursor = connection.cursor()
        query = "UPDATE face_record SET student_id = %s, face_encoding = %s, image_url = %s WHERE id = %s"
        cursor.execute(query, (face_record.student_id, face_record.face_encoding, face_record.image_url, face_record.id))
        connection.commit()
        cursor.close()
        connection.close()

    def remove_face_record(self, face_record_id):
        connection = self.connect()
        cursor = connection.cursor()
        query = "DELETE FROM face_record WHERE id = %s"
        cursor.execute(query, (face_record_id,))
        connection.commit()
        cursor.close()
        connection.close()