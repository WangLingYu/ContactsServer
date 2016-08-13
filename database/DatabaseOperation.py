# coding=utf-8
import sqlite3


class DatabaseOperation:
    cursor = None
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect("/Users/wang/PycharmProjects/ContactsServer/Person")
        self.cursor = self.connection.cursor()

    def createDatabase(self):
        self.cursor.execute('''CREATE TABLE person
    (Id INTEGER PRIMARY KEY  AUTOINCREMENT,
    person_name TEXT NOT NULL,
    person_address TEXT,
    person_phone TEXT NOT NULL,
    person_company_phone TEXT,
    person_home_phone TEXT)''')

    def selectDatabase(self):
        self.cursor.execute("SELECT * FROM person")
        return self.cursor

    def addPerson(self):
        pass

    def deletePerson(self):
        self.cursor.execute('''''')
        self.connection.commit()


if __name__ == '__main__':
    dO = DatabaseOperation()
    dO.selectDatabase()
