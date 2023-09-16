import os
import cv2
from tkinter import *
import numpy as np
import face_recognition
from data.process import get_student

data_face_encodings = []
data_face_names = []

def encode_faces():
    for image in os.listdir('data/imgdata'):
        face_image = face_recognition.load_image_file(f"data/imgdata/{image}")
        face_encoding = face_recognition.face_encodings(face_image)[0]
        data_face_encodings.append(face_encoding)
        data_face_names.append(image)

def compare_and_define(face_encoding):
    if len(data_face_encodings) == 0: return -1
    matches = face_recognition.compare_faces(data_face_encodings, face_encoding)
    face_distances = face_recognition.face_distance(data_face_encodings, face_encoding)
    index = np.argmin(face_distances)
    if matches[index]:
        name = data_face_names[index]
        id = int(name.split('.')[0])
        return id   
    else: return -1

def recognition(frame):
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    temp_face_location = face_recognition.face_locations(small_frame)
    temp_face_encoding = face_recognition.face_encodings(small_frame, temp_face_location)[0]
    id = compare_and_define(temp_face_encoding)
    return id

def framesrecognition(frames):
    ids = []
    resultid = -1
    for i in frames:
        ids.append(recognition(i))
    else:
        max = 0
        for i in ids:
            if ids.count(i)>max:
                resultid = i
                max = ids.count(i)
    return get_student(id= resultid)

def check_face(imgname):
    count = 0
    try:
        frame = face_recognition.load_image_file(f"{imgname}")
        count = count_face(frame)
    except: 
        try:
            frame = face_recognition.load_image_file(f"data/imgdata/{imgname}")
            count = count_face(frame)
        except: pass
    if count == 1: return True
    else: return False

def count_face(frame):
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    temp_face_locations = face_recognition.face_locations(small_frame)
    return len(temp_face_locations)