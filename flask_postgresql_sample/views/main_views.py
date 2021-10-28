from flask import Blueprint, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect

from flask_postgresql_sample.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def helloworld():
    return 'Hello World!'


@bp.route('/')
def index():
    return redirect(url_for('upload.building'))
