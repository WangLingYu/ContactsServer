# coding=utf-8
import sqlite3, model


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

    def selectPerson(self):
        self.cursor.execute("SELECT * FROM person")
        return self.cursor

    def addPerson(self, person):
        self.cursor.execute('INSERT INTO person VALUES (?,?,?,?,?,?)', (
            person.id, person.name, person.address, person.phone, person.company_phone, person.home_phone))
        self.connection.commit()

    def deletePerson(self, person):
        self.cursor.execute('DELETE FROM person WHERE Id = ?', (person.id,))
        self.connection.commit()
