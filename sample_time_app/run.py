from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


# returns date time in UTC
@app.route('/time')
def get_time():
    now = datetime.utcnow()
    current_time = now.strftime("%m/%d/%Y %H:%M:%S")
    return current_time


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
