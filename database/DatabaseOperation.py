# coding=utf-8
import sqlite3


class DatabaseOperation:
    cursor = None
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect("Person")
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
        for x in self.cursor:
            print x

    def addPerson(self):
        pass
        # self.cursor.execute("INSERT INTO person VALUES (10,'王晨','四川省','18383038628','123456789','123456')")
        # self.connection.commit()

    def deletePerson(self):
        self.cursor.execute('''''')
        self.connection.commit()


if __name__ == '__main__':
    dO = DatabaseOperation()
    dO.addPerson()
    dO.selectDatabase()
