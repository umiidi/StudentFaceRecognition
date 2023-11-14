from abc import abstractmethod
import mysql.connector

class AbstractDao:

    @abstractmethod
    def connect(self):
        return  mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "12345",
            database = "studentfacerecognition"
        )