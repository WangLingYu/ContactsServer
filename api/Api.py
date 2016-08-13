# coding=utf-8
from flask import Flask, json

app = Flask(__name__)


@app.route('/index')
def personList():
    return json.dumps(
        [
            {"person_phone": "18383038628", "person_name": "王晨", "person_portrait": "PYTHON"},
            {"person_phone": "15983040391", "person_name": "晨心", "person_portrait": "JAVA"}
        ]
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')