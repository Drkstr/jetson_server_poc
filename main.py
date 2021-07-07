import json
from flask import Flask

app = Flask(__name__)


@app.route('/health')
def health():
    return 'All systems are go!'


@app.route('/readJson')
def health():
    return json.loads("test.json")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
