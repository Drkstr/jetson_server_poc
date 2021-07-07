import json

import flask
from flask import Flask

app = Flask(__name__)


@app.route('/health')
def health():
    return 'All systems are go!'


@app.route('/readJson')
def read_json():
    json_file = open("test.json", )
    return flask.jsonify(json.loads(json_file.read()))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
