from flask import Flask

# 순환 참조 오류를 해결하기 위한 함수
def create_app():
    app = Flask(__name__)

    from .views import main_views, myhome_views
    # app에 등록 시킨다.
    app.register_blueprint(main_views.bp)
    app.register_blueprint(myhome_views.bp)
    return app

