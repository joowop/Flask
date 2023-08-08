from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
'''
1. 내부망 테스트 : ip 고정 => flask run --host=0.0.0.0 --port=포트번호 아무거나
2. 외부에서 접근 하는 방법 외부망 (임시방편임) : 인터넷 -> ngrok -> cmd( ngrok있는 경로로 이동) -> pycharm에서 flask run --host=0.0.0.0 --port=포트번호 아무거나
하고 cnd에서 ngrok hhtp 포트번호 -> 주소 복사해서 알려주면 됨.
'''
# 디비를 위한 과정
db = SQLAlchemy()
migrate = Migrate()


# 순환 참조 오류를 해결하기 위한 함수
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    # flask db init -> 터미널창에서 입력 (디비 초기화)
    # 1. from . import models (커맨드에 flask db migrate) 하게 되면 migrations 안에 versions 안에 내가 만든 모델? 이 수정될 수 있도록 쿼리문이 만들어진다.
    # 2. 커맨드에 flask db upgrade 를 통해 내가 만든 db를 업글하면 디비가 생성된다.
    # sqlite로 디비가 생성되었는지 확인한다.
    # 데이터베이스 열기 -> 디비 생성된거 찾아서 클릭 (question 테이블이 생성되었고 orm으로 디비를 생성할ㄹ경우 alembic_version도 같이 생성되는데 이걸 데이터보기하면
    # 파이참에서의 디비 버전과 실제 알렘빅 버전이랑 같다.

    from .views import main_views, classification_views, chat_views, question_views, answer_views
    # app에 등록 시킨다.
    app.register_blueprint(main_views.bp)
    app.register_blueprint(classification_views.bp)
    app.register_blueprint(chat_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    return app


'''
from flask import Flask

app = Flask(__name__)

# 포트 다음에 오는 주소가 /로 되어있으면 뒤에 있는것을 분석을 하기 시작한다. 이것이 route의 역할  ( http://127.0.0.1:5000/ ... )
@app.route('/') # @ route 밑에 있는 함수가 바로 호출되어 실행된다.
def hello_pybo():
    return 'hello, Pybo'

@app.route('/chatbot')
def chatbot():
    return '나는 챗봇입니다.'


# terminal (커맨드) 에서 flask run 을 하면 동작이다.
# 그전에 초기 설정이 set FLASK_APP=pybo 이 코드를 실행해야한다. -> 안되면 export를 set대신에 넣어서 하면 된다.
# 그 다음 flask run
'''
