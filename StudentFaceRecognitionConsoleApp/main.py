from src.data.fileprocess import start_file_process
from src.face.face import encode_faces
from src.face.recognition import run

def start():
    start_file_process()
    encode_faces()
    run()

start()