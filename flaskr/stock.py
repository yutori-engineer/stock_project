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

bp = Blueprint("stock", __name__)

@bp.route("/stock/")
# @simple_page.route('/practice/<page>')
def stock():
    try:
        return render_template(f'stock.html')
        # return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)