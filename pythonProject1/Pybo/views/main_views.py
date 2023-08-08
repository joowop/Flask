from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from Pybo.models import Question

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def index():
    # main에 접속하면 question_views에 바로 접근하게 만들기 (리 다이렉트)
    return redirect(url_for('question.q_list'))

# set FLASK_DEBUG=true -> true로 바꿔주면 터미널이 켜져있으면 수정해도 적용이 된다.

@bp.route('/meta')
def main_meta():
    return '메타버스아카데미 ai'