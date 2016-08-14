# coding=utf-8
from flask import Flask, url_for, request, render_template
import database, model
import json

app = Flask(__name__)


@app.route('/<string:customer_id>/contacts')
def getPersonList(customer_id):
    if customer_id == '1':
        dO = database.DatabaseOperation()
        cursor = dO.selectPerson()

    persons = []

    for result in cursor:
        persons.append({'person_id': result[0],
                        'person_name': result[1],
                        'person_address': result[2],
                        'person_phone': result[3],
                        'person_company_phone': result[4],
                        'person_home_phone': result[5]}
                       )

    return json.dumps(persons)


@app.route('/<string:customer_id>/addPerson', methods=['POST'])
def addPerson(customer_id):
    if customer_id == '1':
        person = model.Person()
        jsonData = request.get_json()
        person.id = jsonData['person_id']
        person.name = jsonData['person_name']
        person.address = jsonData['person_address']
        person.phone = jsonData['person_phone']
        person.company_phone = jsonData['person_company_phone']
        person.home_phone = jsonData['person_home_phone']
        dO = database.DatabaseOperation()
        dO.addPerson(person)
        return json.dumps({'status': 'success'})


@app.route('/<string:customer_id>/deletePerson', methods=['POST'])
def deletePerson(customer_id):
    if customer_id == '1':
        person = model.Person()
        jsonData = request.get_json()
        person.id = jsonData['person_id']
        dO = database.DatabaseOperation()
        dO.deletePerson(person)
        return json.dumps({'status': 'success'})


@app.route('/login', methods=['POST'])
def login():
    result = request.get_json()

    account = result['account']
    password = result['password']
    if account is not None and password is not None:
        if account == 'wangchen' and password == '123456':
            return json.dumps({'status': 'success', 'customer_id': '1'})
        else:
            return {'status': 'falied', 'customer_id': None}
    else:
        return {'status': 'falied', 'customer_id': None}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
