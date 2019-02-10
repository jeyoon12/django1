
'''
* form 
- HTML의 <form> 태그에 들어가는 <input> 태그들을 관리하는 클래스/기능
- 양식을 수정하고 싶을 때 변수들을 통해 알아서 입력 양식이 구성되도록, 그리고 버전 관리를 용이하게 하기 위해 사용
- 모델 클래스에 저장된 변수들에 맞춰 자동 설정도 할 수 있고, 커스텀 입력 공간(모델 클래스와 연동 x)도 
    생성할 수 있음  ex. 회원 가입 시 비밀번호 확인 칸은 굳이 DB에 저장할 필요 없음

사용 방법: class 클래스명 (ModelForm 또는 Form):
ModelForm: 모델클래스를 기반으로 입력 양식을 자동 생성할 때 상속받는 클래스
Form: 커스텀 입력 양식을 생성할 때 상속받는 클래스
ModelForm을 상속받았을 때도 커스텀 입력 양식을 생성할 수 있음

폼 클래스의 객체를 함수를 통해 HTML 문서의 코드로 변환할 수 있음 (<p>, <table>, <li>)
ex) 폼클래스 객체.as_p() -> 해당 폼 객체에 저장된 입력 공간들을 <input> 태그로 변환하고, 
개별적으로 <p> 태그로 묶은 문자열을 반환
ex2) 회원가입 폼 클래스 객체.as_p()
-> """<p> <label>아이디</label> <input type="" name=""> </p>
      <p> <label>비밀번호</label> <input type="" name=""> </p>""" 문자열 반환

* 개발 방법
1) ModelForm/Form 클래스 임포트
2) 사용할 모델클래스 임포트
3) ModelForm/Form 클래스를 상속받은 폼클래스 정의

만들어진 폼클래스는 View에서 객체 생성을 통해 활용함

* 기존 개발 순서
- 어플리케이션 생성 -> settings.py 등록 -> 모델 정의 -> DB 반영 -> 뷰정의 -> 템플릿 정의
-> URLConf 등록

* 변경
- 어플리케이션 생성 -> settings.py 등록  -> 모델 정의 -> DB 반영 -> 폼클래스 정의 -> 뷰 정의
-> 템플릿 정의 -> URLConf 등록
'''
from django.forms.models import ModelForm
# 실제 개발 시 modelform 써서 자동 양식 누르면 알아서 import 해줌

from .models import Question, Choice
# Question 모델 클래스와 연동된 모델 폼클래스 정의 (Question 객체 추가/수정 시 사용)
class QuestionForm(ModelForm):
    class Meta: # Meta 클래스: 연동하고자 하는 모델클래스에 대한 정보를 정의하는 클래스
        # Meta 클래스에서는 아래와 같은 세가지 변수 사용 가능
        # model: 연동하고자 하는 모델클래스를 저장하는 변수
        model = Question # QuestionForm이 Question 클래스와 연동하겠다는 의미
        
        # fields: 모델클래스에서 정의된 변수 중 어떤 변수를 클라이언트가 작성할 수 있도록 
        # 입력 양식으로 제공할 것인지 지정하는 변수 (iterable - list, tuple)
        # exclude: 모델클래스에 정의된 변수 중 입력 양식으로 만들지 않을 것을 지정하는 변수(list)
        # fields, exclude 변수 중 한개만 사용해야 하므로 적절히 선택해 사용
        fields = ['name'] # name 변수만 입력할 수 있는 form 생성
        # exclude = ['date'] # date 변수를 제외한 모든 변수 입력할 수 있는 form 생성
        
        
# Choice 모델클래스와 연동된 모델 폼클래스 정의 (Choice 객체 추가/수정 시 사용)
class ChoiceForm(ModelForm):
    # Choice 모델클래스 연동 및 q 변수와 name 변수를 클라이언트가 입력할 수 있도록 설정
    class Meta:
        model = Choice
        # exclude = ['votes'] -> 좀더 유동적임. 새로운 변수가 생성돼도 변동 가능하므로
        fields = ['q', 'name'] # q, name 반대로 쓰면 웹에서도 반대로 보임





