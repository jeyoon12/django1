from django.db import models

# 질문
# 질문제목 생성일
class Question(models.Model):
    name = models.CharField('질문제목', max_length=100)
    # DateField: 날짜(년월일)를 저장하는 공간
    # DateTimeField: 날짜와 시간을 저장하는 공간 
    date = models.DateTimeField('생성일')
    def __str__(self):
        return self.name
    class Meta: # 모델클래스에 정의된 변수, 테이블 이름 등을 처리할 때 사용하는 클래스
        # ordering : 해당 모델클래스에 정의된 변수 중에서 정렬에 사용할 변수이름을 저장하는 변수
        # 변수이름만 쓴 경우 -> 오름차순, '-' 변수이름 쓴 경우 -> 내림차순
        ordering = ['-date'] # 가장 최근에 만들어진 객체 순으로 정렬
        # models에서 가져온 meta의 경우 따로 migrate 안해줘도 됨
        # views.py의 Question 객체를 사용자가 수정하는 뷰 주석으로 이동 

# 답변
# 어떤 질문에 연결돼있는지, 답변 내용, 투표수 
class Choice(models.Model):
    
    # ForeignKey(연결할 다른 모델클래스): ForeignKey 객체를 만든 모델클래스의 객체들이
    # 연결한 모델클래스의 객체와 n:1 관계로 연결할 수 있는 설정(하나의 question에 여러개의 답변이 연결)
    # ForeignKey의 객체를 저장한 변수는 연결한 모델클래스의 객체를 저장하는 변수가 됨
    # Choice객체.q.name -> 해당하는 Choice객체와 연결된 Question 객체의 name 변수값을
    # 추출(q가 Question의 객체가 됨)
    # on_delete: 연결된 모델 클래스의 객체가 삭제될 때 어떻게 처리할 지 지정하는 변수
    # on_delete = models.PROTECT: 연결된 모델클래스의 객체가 삭제되지 않도록 막아주는 역할
    # models.CASCADE: 연결된 모델클래스의 객체가 삭제되면 같이 삭제됨
    # models.SET_NULL: 연결된 모델클래스의 객체가 삭제되면 아무것도 연결되지 않은 상태로 유지
    # models.SET(연결할객체): 연결된 객체가 삭제되면 매개변수로 넣은 객체와 연결
    # models.SET_DEFAULT: 연결된 객체가 삭제되면 기본 설정된 객체와 연결
    q = models.ForeignKey(Question, on_delete = models.CASCADE)
    # foreignkey는 이름 변경 못함
    name = models.CharField('답변항목', max_length=50)
    
    # IntegerField: 정수값을 저장하는 공간
    # default: 모델클래스의 객체 생성 시 해당 저장공간에 기본값 설정
    # default는 모든 Field에서 사용할 수 있음
    votes = models.IntegerField('투표수', default=0)
    
    def __str__(self):
        return self.q.name + ' / ' + self.name