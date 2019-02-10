
# 하위 URLConf
# app_name : 하위 URLConf 파일의 등록된 URL들의 그룹명
# urlpatterns : URL과 뷰함수를 리스트형태로 등록하는 변수
# => 위의 두가지 변수는 반드시 생성해야 URLConf로 사용 가능
from django.urls import path # 이 부분 추가해야 됨(상위 urls.py에는 자동 생성되므로 참고)
from .views import *
# 위에서 너무 길어져 *로 처리(index, detail, result, vote, qregister, qupdate, qdelete)

app_name = 'vote' # 이름은 자유롭게 만들 수 있음

# 기본 주소: 127.0.0.1:8000/vote/
urlpatterns = [ # 자동완성 쓰면 안됨. import 하면 안돼서
    # 웹 클라이언트가 127.0.0.1:8000/vote/ 요청 시 index 뷰함수 호출
    # name: 해당 URL, 뷰함수 등록에 대해 별칭을 지정
    path('', index, name= 'index'),
    # 127.0.0.1:8000/vote/숫자/
    path('<int:q_id>/', detail, name='detail'),
    path('vote/', vote, name='vote'),
    path('result/<int:q_id>/', result, name='result'),
    path('qr/', qregister, name='qr'),
    # 127.0.0.1:8000/vote/qr로 페이지 들어가보고 그 다음 views.py로 이동
    path('qu/<int:q_id>/', qupdate, name='qu'), # qu는 매개변수 추가 요구해서 int 추가
    # 127.0.0.1:8000/vote/qu/Question 객체의 id 값 실행하고 views.py Question 객체 삭제로 이동
    path('qd/<int:q_id>/', qdelete, name='qd'),
    # 127.0.0.1:8000/vote/qd/Question 객체의 id 값 실행하고 index.html 이동해 삭제 링크 만들기
    path('cr/', cregister, name='cr'),
    # 127.0.0.1:8000/vote/cr/ 실행 후 views.py의 choice 수정으로 이동
    path('cu/<int:c_id>/', cupdate, name='cu'),
    # 127.0.0.1:8000/vote/cu/choice객체 id값 확인해보기 id값은 관리자페이지 - 
#     choice에서 해당 choice 선택했을 때 뜨는 url로 확인
    # index.html로 이동해서 각 choice옵션에 수정 추가
    path('cd/<int:c_id>', cdelete, name='cd'),
    # 
    ]

# 그 다음 플젝에 있는 상위 urls.py에 등록해야 함

