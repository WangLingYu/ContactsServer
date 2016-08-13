# coding=utf-8
from flask import Flask, json
import database

app = Flask(__name__)


@app.route('/index')
def personList():
    dO = database.DatabaseOperation()
    cursor = dO.selectDatabase()

    return json.dumps(
        [
            {"person_phone": "18383038628", "person_name": cursor[0][1], "person_portrait": "PYTHON"},
            {"person_phone": "15983040391", "person_name": "晨心", "person_portrait": "JAVA"}
        ]
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
