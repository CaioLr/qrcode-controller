from flask import Flask, send_file
import uuid
from flask import Blueprint, render_template
from .helpers import getQRcode
from .events import create_session


bp = Blueprint("main", __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/controller/<uuid>')
def controller(uuid):
    return render_template('controller.html',uuid=uuid)

@bp.route('/set/')
def set():
    id = uuid.uuid4()
    img = getQRcode(id)

    create_session(id)

    return send_file(img, mimetype='image/jpeg')

