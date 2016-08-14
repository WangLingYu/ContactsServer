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
        persons.append({'person_id': result[0],
                        'person_name': result[1],
                        'person_address': result[2],
                        'person_phone': result[3],
                        'person_company_phone': result[4],
                        'person_home_phone': result[5]}
                       )

    return json.dumps(persons)


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
