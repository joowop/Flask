from flask import Blueprint
from flask import request
# 디비에 데이터 넣고싶을떄
from Pybo.models import Question, Answer
from datetime import datetime
from Pybo import db
# torch 여기에는 그냥 torch cpu로 설치하겠다. 인터넷 가서 torch 설치에서 cpu 누르면 pip3 install torch torchvision torchaudio 이런게 뜨는데 커맨드에 이거 읿력
import torch
from torchvision import transforms
from PIL import Image

bp = Blueprint('classification',__name__,url_prefix='/classification')

# 연예인 분류 모델 불러오기
# 이 모델은 gpu환경에서 학습 시킨 모델이기때문에 map_location=torch.device('cpu') 추가
model = torch.load('model.pt', map_location=torch.device('cpu'))

@bp.route('/')
def classification():

    return 'classification Page!'

@bp.route('/catdog')
def catdog():
    result = request.form
    print(result)
    print(result['chat'])
    return '고양이 입니다.'

@bp.route('/birdflower')
def birdflower():
    # 생성한 디비에 데이터를 넣고 싶을 때
    q = Question(subject='질문3', content='고양이 맞나요?',create_date= datetime.now())
    # 데이터베이스에 넣어라
    db.session.add(q)
    db.session.commit()


    return '비둘기 입니다.'

# db CRUD 방법
@bp.route('/get_question')
def get_question():
    # question이라는 테이블의 데이터를 모두(전체) 가져온다. , [question1, question2 ...]
    # questions = Question.query.all()
    # print(len(questions))

    # id로 가져오기
    # result = Question.query.filter(Question.id==1).all()
    # result = Question.query.filter(Question.content.like('%고양이%')).all()
    # print(result[0].subject)
    # print(result[0].content)

    # 수정하는 방법
    # result = Question.query.get(1) # pk값이 1인 데이터를 가져와라
    # result.subject = '제목을 바꿈 1'
    # db.session.commit()

    # 삭제하는 방법
    result = Question.query.get(1)
    db.session.delete(result)
    db.session.commit()
    return '가져오기 성공'


@bp.route('/manwoman')
def manwoman():
    return '여성입니다.'


# 연예인 이미지 분류기 모델 보내기 서로 공유 마동석 사진 보내면 모델이 돌아가도록
# post방식으로 접근해야 된다.
@bp.route('/makale',methods = ['POST'])
def classification_makale():
    # psotman에서(client)가 데이터(파일)를 보내준것을 확인할 수 있는 코드
    print(request.files)
    # image라는 key값 받기
    f = request.files['image']
    print(f.filename)
    f.save('image.jpg')
    image = Image.open('image.jpg')

    # 학습 시킨 환경과 똑같이 맞춰주기 위한 코드
    transform_test = transforms.Compose([
        transforms.Resize((244,244)), # 괄호 조심..!
        transforms.ToTensor(),
        transforms.Normalize( mean = [0.485,0.456,0.406], std = [0.229,0.224,0.225])
    ])
    # 차원도 맞추기위해 unsqeeze
    image = transform_test(image).unsqueeze(0).to('cpu')
    model.to('cpu')

    # 추론
    with torch.no_grad():
        outputs = model(image)
        print(outputs)
        # 모델에서 추론 된 가장 큰 값 구하기
        _, preds = torch.max(outputs,1)
        classname = ['마동석', '이국주', '카리나']
        print(classname[preds[0]])

    return classname[preds[0]] + ' 입니다.'

# 1. postman에서 makale 주소에서 body (text에서 file로 바꿔주고)-> key에 image라는 이름으로 value는 마동석 사진 하나 다운받아서 넣어준다.
# 2. postman에서 get 방식을 post 방식으로 바꿔준다.
