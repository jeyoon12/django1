# views.py: view의 기능을 하는 클래스/함수를 정의하는 파일

# render (함수): 웹 클라이언트에게 HTML 파일을 넘겨줄 때 사용하는 함수
from django.shortcuts import render

# 뷰 함수 정의 시 첫번째 매개변수를 request로 설정해야 함
# request: 사용자의 요청 정보, <form>으로 넘겨준 데이터, 로그인정보, 세션정보, 
# 요청방식(get/post) 등이 저장됨
            
# HTML 파일을 전송하는 메인페이지
def index(request):
    # render(request(매개변수), 클라이언트에게 줄 HTML 파일경로, HTML에 전달할 값)
    return render(request, 'bookmark/index.html', 
                  {'a':"hello 장고", 'b':[1,2,3,4,'django']})
    # -> bookmark에 전달할 index.html가 없으면 500번대 에러 뜸

# bookmark 모델클래스 임포트
from .models import Bookmark
# from bookmark.models import Bookmark -> 절대 경로 위는 상대 경로

# Bookmark 모델클래스에 저장된 모든 객체를 HTML에 추가하는 페이지
def booklist(request):
    '''
    1. 모델클래스.objects.get() : DB에 해당 모델 클래스로 저장된 객체 중 특정 조건을 만족하는 
              객체 한 개를 추출하는 함수
    2. 모델클래스.objects.all() : DB에 해당 모델클래스로 저장된 모든 객체를 추출
    3. 모델클래스.objects.filter() : DB에 저장되는 특정 조건을 만족하는 모든 객체를 
              리스트 형태로 추출
    4. 모델클래스.objects.exclude() : DB에 특정 조건을 만족하지 않는 모든 객체를 
              리스트 형태로 추출
    '''
    # Bookmark 모델클래스의 모든 객체를 리스트 형태로 list 변수에 저장
    list = Bookmark.objects.all()
    return render(request, 'bookmark/booklist.html', {'objt' : list})
    # booklist.html이 없으므로 templates - bookmark 우클릭 - new - 
    # other - html - 이름: booklist 후 booklist.html로 이동

# Bookmark 모델 클래스의 객체 중 한개를 HTML에 추가하는 페이지
# 뷰함수에 매개변수 추가 시, URLConf에서 추가 설정을 해야함
def getbook(request, bookid):
    # 객체 한개를 추출할 때, 객체별로 저장된 고유한 id값을 이용해 추출함
    # 어떤 id 값을 가진 객체를 요청했는지 알아야 됨
    # => view 함수의 매개변수를 늘림, <form>로 넘어온 데이터 처리
    # 데이터베이스에 저장된 Bookmark 객체들 중 id 변수에 저장된 값이 bookid 값과 동일한 객체를
    # 한개 추출해 obj 변수에 저장
    obj = Bookmark.objects.get(id=bookid)
    print(obj)
    return render(request, 'bookmark/getbook.html', {'book': obj})
    # getbook html 생성: templates - bookmark 우클릭 - new - other 
    # - 이름: getbook



