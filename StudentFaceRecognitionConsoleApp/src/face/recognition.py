import face_recognition
import cv2
from src.face.face import compare_and_define


def run():
    video_capture = cv2.VideoCapture(0)
    process_current_frame = True
    while True:
        ret, frame = video_capture.read()
        if process_current_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            temp_face_locations = face_recognition.face_locations(small_frame)
            temp_face_encodings = face_recognition.face_encodings(small_frame, temp_face_locations)
            temp_face_names = compare_and_define(temp_face_encodings)
        process_current_frame = not process_current_frame

        for (top, right, bottom, left), name in zip(temp_face_locations, temp_face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) == ord('\t'): break
    video_capture.release()
    cv2.destroyAllWindows()
