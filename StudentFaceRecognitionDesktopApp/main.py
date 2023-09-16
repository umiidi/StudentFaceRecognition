from app import start_app
from data.config import read_config
from data.recognition import encode_faces

def start():
    read_config()
    encode_faces()
    start_app()

if __name__ == "__main__":
    start()