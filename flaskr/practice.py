import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import abort
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from jinja2 import TemplateNotFound
from .db import get_db

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/practice', defaults={'page': 'index'})
# @simple_page.route('/practice/<page>')
def show(page):
    try:
        return render_template(f'practice.html')
        # return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)