# models.py: 모델 클래스를 정의할 때 사용하는 파일
# models: 모델 클래스를 정의할 때 사용하는 클래스가 정의된 파이썬 파일
from django.db import models 


# 모델 클래스 개발 및 반영 순서
'''
1) 모델 클래스 정의 시, models.Model 클래스 상속받아 모델클래스를 정의
      참고) ctrl 누른 상태에서 클래스에 커서 올리면 그 안의 클래스 확인 가능
      
2) 생성한 모델 클래스를 manage.py에 makemigrations 명령으로 migration 파일 생성
3) manage.py에 migrate 명령으로 데이터베이스에 실질적인 저장공간 생성
'''
# class 클래스명(models.Model): 모델 클래스 정의

# 북마크를 저장할 모델 클래스
# URL 이름(파란글씨), 클릭 시 넘어갈 URL 주소 저장

class Bookmark(models.Model):
    # 클래스 변수를 생성해 해당 모델 클래스가 어떤 값들을 저장하는지 정의
    # 클래스변수 = models.xxxxFields 클래스의 객체를 저장하는 것으로 저장 공간을 정의
    # Char(앞 글자 대문자이므로 클래스): 글자수 제한이 있는 문자열을 저장하는 공간을 정의
    # max_length : 최대 저장할 수 있는 글자 수
    name = models.CharField(max_length=20)
    # URLField: 인터넷 주소(URL)을 저장하는 공간을 정의
    url = models.URLField()
    
    # __str__: 객체를 출력할 때 (print(객체)) 표현 방식을 처리하는 파이썬 함수
    # Model 클래스에 구현된 __str__ 함수를 오버라이딩해 표현 방식 변경
    # 함수 추가/변경(오버라이딩)을 하는 작업은 makemigrations/migrate할 필요 없음
    
    def __str__(self):
        # 상속받은 클래스의 함수호출: super().__str__()
        #                    models.Model.__str__(객체) -> 특정한 클래스의 함수
        # models.Model의 ctrl + 커서를 옮겨 __str__ 구성을 확인
        return self.name

    











