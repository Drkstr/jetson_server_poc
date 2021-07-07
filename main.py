import json
import flask
from flask import Flask
from flask import send_file

app = Flask(__name__)


@app.route('/health')
def health():
    return 'All systems are go!'


@app.route('/readJson')
def read_json():
    json_file = open("test.json", )
    return flask.jsonify(json.loads(json_file.read()))


@app.route('/getImage')
def get_image():
    return send_file("test_image.jpeg", mimetype='image/gif')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
