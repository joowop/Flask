from flask import Blueprint, render_template, request, url_for
from Pybo.models import Question
from Pybo.forms import QuestionForm
from datetime import datetime
from Pybo import db
from werkzeug.utils import redirect

bp = Blueprint('question',__name__,url_prefix='/question')

# 웹 게시판 만들기
@bp.route('/list/')
def q_list():
    # 데이터 가져오기
    question_list = Question.query.order_by(Question.create_date.desc()) # 최신 날짜부터
    return render_template('question/question_list.html', question_list=question_list) # html페이지를 불러오기 위해서 사용

@bp.route('/detail/<int:question_id>') # detail 주소 뒤에 question_id 라는 int형 변수를 쓰겠다.
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question = question)

@bp.route('/create/', methods=['GET', "POST"])
def create():
    form = QuestionForm()
    print(request.method)
    print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content = form.content.data, create_date = datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form = form)