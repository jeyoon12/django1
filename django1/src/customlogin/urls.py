# 작성 시 자동완성 사용하면 안됨
from django.urls import path
from .views import *

app_name = 'cl'
# 기본주소: 127.0.0.1:8000/cl/

urlpatterns = [# 기본 양식 세팅 후 django1의 urls.py로 이동해 코드 등록
               path('signup/', signup, name='signup'),
               # 저장 후 127.0.0.1:8000/cl/signup/ 실행하고 views.py의 로그인 처리
               path('signin/', signin, name="signin"),
               # 저장 후 127.0.0.1:8000/cl/signin/ 실행
               path('signout/', signout, name="signout"),
               # 저장 후 127.0.0.1:8000/cl/signout/ 실행 
               # -> 확인 방법은 관리자 페이지로 이동했을 때 로그인하라는 페이지 뜨면 됨
               # 그 다음 forms.py의 class signupform로 이동
               
    
    ]

