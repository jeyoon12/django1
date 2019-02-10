"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # 위 주석 참조해 다른 urlconf 등록을 위해 include 포함

# bookmark/views.py의 index, booklist 함수 추가 (서로 다른 파일 내에 있으므로 '.' 사용 불가)
from bookmark.views import index, booklist, getbook # 노란 줄이 뜨는 것은 이거 사용 안했다는 의미
# from bookmark.views import * => 해당 파일에 들어있는 모든 변수, 함수, 클래스 import

# url.py: 웹클라이언트의 요청을 분석해 특정한 뷰를 호출하는 역할
# urlpatterns: URL과 뷰함수를 등록 및 관리하는 변수
# 리스트 형태로 저장. URL 등록 시 path 함수를 통해 urlpatterns의 요소로 추가

# path(URL주소(문자열), 호출할 뷰함수/클래스 이름)


# 기본 주소: 127.0.0.1:8000
urlpatterns = [
    # 웹 클라이언트가 127.0.0.1:8000/admin으로 요청한 경우
    # 관리자 사이트 뷰가 실행되도록 등록
#     path('admin/', admin.site.urls) => 관리자 사이트 홈페이지 주소 /a1으로 변경됨
    path('a1/', admin.site.urls),
    # 웹 클라이언트가 127.0.0.1:8000/ 으로 요청한 경우 index 뷰함수 호출
    path('', index),
    path('booklist/', booklist),
    # 127.0.0.1:8000/숫자값/으로 요청한 경우 getbook 뷰함수 호출.
    # bookid 매개변수에 숫자값을 대입
    # URL에서 매개변수로 사용할 값을 분리하는 방법 : <값의 타입:매개변수이름>
    path('<int:bookid>/', getbook),
    # 투표 어플리케이션에 사용할 하위 URLConf 등록
    # 웹클라이언트가 127.0.0.1:8000/vote/로 시작하는 모든 요청을
    # vote 폴더에 있는 urls.py에 등록된 urlpatterns로 처리하도록 등록
    path('vote/', include('vote.urls')),
    #127.0.0.1:8000/cl/로 시작하는 모든 요청을 customlogin/urls.py에 넘겨줌
    path('cl/', include('customlogin.urls')),
    # django1의 settings.py의 installed_app로 이동
    path('blog/', include('blog.urls')),
    #127.0.0.1:8000/blog로 시작하는 모든 요청을 blog/urls.py로 처리
    
    # social_django 어플리케이션의 하위 URLConf 등록
    path('auth/', include('social_django.urls', namespace='social'))
    # customlogin - templates - cl - signin.html로 이동 
]

# 위의 path('', index) 설정 후 좌상단 전체 저장 아이콘 누른 후 127.0.0.1:8000 접속해보기
# 그 다음 views.py로 이동 Bookmark 모델클래스에 저장된 모든 객체를 HTML에 추가하는 페이지로
# bookmark html 등록 후 path('booklist'~) 접속되는 지 확인 후 views.py 이동
# getbook 접속 확인 시 주소 뒤에 /1~3/ 중 하나만 넣어야 함 나머지 숫자는 오류(등록이 세개밖에 안되서)


# 미디어 파일을 저장 및 요청 처리하기 위한 설정

# setting.py에 설정된 변수를 가져오기 위해 임포트
from django.conf import settings
# MEDIA_URL과 MEDIA_ROOT를 연결하기 위한 함수
from django.conf.urls.static import static
# 파일 요청 URL과 실제 저장된 파일 경로를 매칭
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# django1 우클릭해 django - make migrations 눌러 이름: blog로 확인 눌러 
# blog 아래 migrations 파일에 0001_initial.py 생겼는지 확인
# 그 다음 똑같은 곳에서 migrate 누르면 콘솔에 applying blog.0001_initial... ok 떠야함
# 그 다음 blog의 admin.py로 이동
