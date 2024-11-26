from flask import Flask, session, send_file
from flask_session import Session
from config import AppConfig
from helpers import getQRcode
import uuid


app = Flask(__name__)
app.config.from_object(AppConfig)

server_session = Session(app)


@app.route('/')
def home():
    return 'Opa'

@app.route('/controller/<uuid>')
def controller(uuid):
    return 'Sim'

@app.route('/set/')
def set():
    id = uuid.uuid4()
    img = getQRcode(id)
    return send_file(img, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)