import os
import numpy as np
import face_recognition
from src.data.studentlist import name_request


data_face_encodings = []
data_face_names = []

def encode_faces():
    for image in os.listdir('src/imgdata'):
        face_image = face_recognition.load_image_file(f"src/imgdata/{image}")
        face_encoding = face_recognition.face_encodings(face_image)[0]
        data_face_encodings.append(face_encoding)
        data_face_names.append(image)

def compare_and_define(temp_face_encodings):
    temp_face_names = []
    if len(data_face_encodings) == 0: return ["Unknown"] * len(temp_face_encodings)
    for face_encoding in temp_face_encodings:
        matches = face_recognition.compare_faces(data_face_encodings, face_encoding)
        name = None
        face_distances = face_recognition.face_distance(data_face_encodings, face_encoding)
        index = np.argmin(face_distances)
        if matches[index]:
            name = data_face_names[index]
        temp_face_names.append(f'{name_request(name)}')
    else:
        return temp_face_names
