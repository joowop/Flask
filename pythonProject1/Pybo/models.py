from Pybo import db

# 밑의 클래스들은 각 클래스가 디비 테이블이다.
class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 질문이 quesuion_id 3번이 삭제가 되면 알아서 이것도 삭제해라 ondelete='CASCADE'
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
