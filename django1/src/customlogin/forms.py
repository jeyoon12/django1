
# django에서 제공하는 auth 어플리케이션의 models.py 임포트
from django.contrib.auth.models import User
from django.forms import ModelForm # DB 저장 시 사용 공간
from django import forms # 커스텀 입력 양식을 위해 추가. input 태그 만들 때 사용하는 공간
# 회원가입에 사용할 모델 폼 클래스
class SignupForm(ModelForm):
    
    # 생성자 오버라이딩: password_check 변수의 label 수정
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 상속받은 클래스의 생성자 호출
        # password_check 변수의 label 속성 수정
        self.fields['password_check'].label = '비밀번호 확인'
        # 그 다음 아래 <input>의 순서를 지정으로 이동

    
    # 모델클래스에 없는 입력 양식을 생성 : 커스텀 입력 양식
    # forms에 들어있는 xxxfield 클래스의 객체를 클래스 변수에 저장해 커스텀 입력 양식을 생성할 수 있음
    # 모델 클래스의 저장 공간을 생성하는 것과 유사하나 서로 다른 기능을 만들 때 사용함
    
    # forms에 들어있는 xxxInput 클래스의 객체를 widget으로 지정하면 해당 타입으로 입력 양식이 생성됨
    
    # 비밀번호 확인
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    
    # <input>의 순서를 지정
    field_order = ['username', 'password', 'password_check', 'last_name', 
                   'first_name', 'email']

    class Meta:
        model = User
        
        widgets = {
            'password' : forms.PasswordInput()
            }
        
        # ID, 비밀번호, 성, 이름, 이메일
        fields = ['username', 'password', 'last_name', 'first_name', 
                  'email'] # 무엇이 존재하는지 확인하기 위해서는 document 확인 필요함
        # 위에서 언급되는 변수 순서 바꾸면 배치도 자동으로 바뀜


# 로그인에 사용할 모델 폼 클래스
class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        #customlogin - views.py로 이동






