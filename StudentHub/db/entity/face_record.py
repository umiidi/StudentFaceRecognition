class FaceRecord:
    def __init__(self, id, student_id, face_encoding, image_url) -> None:
        self.id = id
        self.student_id = student_id
        self.face_encoding = face_encoding
        self.image_url = image_url

    def __str__(self) -> str:
        return f"FaceRecord{{id: {self.id}, student_id: {self.student_id}, face_encoding: {self.face_encoding}, image_url: {self.image_url}}}"