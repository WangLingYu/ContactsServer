# coding=utf-8
from flask import Flask, url_for, request
import database, model
import json

app = Flask(__name__)


@app.route('/<string:customer_id>/contacts')
def getPersonList(customer_id):
    if customer_id == '1':
        dO = database.DatabaseOperation()
        cursor = dO.selectDatabase()
        persons = []
        for result in cursor:
            person = model.Person()
            person.id = result[0]
            person.name = result[1]
            person.address = result[2]
            person.phone = result[3]
            person.company_phone = result[4]
            person.home_phone = result[5]
            persons.append(person)
        return json.dumps(
            [
                {'person_id': persons[0].id,
                 'person_name': persons[0].name,
                 'person_address': persons[0].address,
                 'person_phone': persons[0].phone,
                 'person_company_phone': persons[0].company_phone,
                 'person_home_phone': persons[0].home_phone},
                {
                    'person_id': persons[1].id,
                    'person_name': persons[1].name,
                    'person_address': persons[1].address,
                    'person_phone': persons[1].phone,
                    'person_company_phone': persons[1].company_phone,
                    'person_home_phone': persons[1].home_phone},
            ]
        )


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
