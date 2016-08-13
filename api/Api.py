# coding=utf-8
from flask import Flask, url_for, request
import database, model
import json

app = Flask(__name__)


@app.route('/<string:customer_id>/contacts')
def getPersonList(customer_id):
    dO = database.DatabaseOperation()
    dO.selectDatabase()

    if customer_id == '1':
        return json.dumps(
            [
                {"person_phone": "18383038628", "person_name": "王晨", "person_portrait": "PYTHON"},
                {"person_phone": "15983040391", "person_name": "晨心", "person_portrait": "JAVA"}
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
