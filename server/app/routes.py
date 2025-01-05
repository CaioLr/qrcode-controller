from flask import Flask, make_response, send_file, Blueprint, render_template, jsonify
import uuid
from .helpers import getQRcode
from .events import create_session


bp = Blueprint("main", __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/controller/<uuid>')
def controller(uuid):
    return render_template('controller/index.html',uuid=uuid)

@bp.route('/set/')
def set():
    id = uuid.uuid4()
    img = getQRcode(id)

    create_session(id)

    response = make_response(send_file(img, mimetype='image/jpeg'))
    response.headers['uuid'] = str(id)

    return response
