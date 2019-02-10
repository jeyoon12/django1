# admin.py: 해당 어플리케이션에 정의된 모델클래스를 관리자 사이트에서
# 데이터 추가/수정/삭제할 수 있도록 설정하는 파일

from django.contrib import admin
# 현재폴더(.)에 models.py 안의 Bookmark 모델클래스를 임포트
# from 뒤에 . 누르면 현재 나와 같은 폴더에 있는 모듈 보여줌

from .models import Bookmark

admin.site.register(Bookmark)
# admin.site.register(모델클래스명)

# 저장 후 관리자 사이트 새로고침하면 bookmark 확인 가능
# bookmarks 클릭해 네이버와 url 입력해 저장 누르면 객체 생성 확인 가능
# 총 세 개 bookmark 객체 추가하기
# bookmark object 뒤에 (1), (2), (3)는 아이디 값을 부여했다고 보면 됨