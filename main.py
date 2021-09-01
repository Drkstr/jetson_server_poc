import json
import flask
from flask import Flask
from flask import send_file
from flask import jsonify, make_response


app = Flask(__name__)


@app.route('/')
def name():
    response = flask.Response("Jeton 1")
    return response

@app.route('/health')
def health():
    response = flask.Response("All systems are go!")
    return response


@app.route('/getJson')
def read_json():
    json_file = open("test.json", )
    # return flask.jsonify(json.loads(json_file.read()))
    return make_response(jsonify(json.loads(json_file.read())))


@app.route('/getImage')
def get_image():
    return make_response(send_file("test_image.jpeg", mimetype='image/gif'))


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

