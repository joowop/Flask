from flask import Blueprint

bp = Blueprint('myhome',__name__,url_prefix='/myhome')

@bp.route('/main')
def myhome_main():
    return 'myhome_main 입니다.'

