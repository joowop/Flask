from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect


bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def index():
    # main에 접속하면 question_views에 바로 접근하게 만들기 (리 다이렉트)
    return render_template('index.html')
