
from .models import Post
from django import forms

# 글쓰기에 사용할 폼클래스 - 모델폼클래스 상속
class PostForm(forms.ModelForm):
    # 사용자가 첨부파일, 이미지를 업로드할 수 있도록 커스텀 입력 양식 생성
    # required=False: 해당 <input>을 사용자가 필수로 입력하지 않아도 되는 설정
    # => 첨부 파일을 꼭 업로드하지 않아도 되는 설정
    # ClearableFileInput: <input type='file'> 형태의 입력 공간에 파일 관련 추가 설정을 할 수 있는 위젯
    # multiple: 하나의 입력 공간에 여러 개의 파일을 업로드할 수 있도록 허용
    
    files = forms.FileField(required=False, 
                            widget=forms.ClearableFileInput(attrs={'multiple':True}))
    
    images = forms.ImageField(required=False, 
                              widget=forms.ClearableFileInput(attrs={'multiple':True}))
    
    class Meta:
        model = Post
        fields = ['category', 'headline', 'content'] 
        # 어떤 변수 넣어야 할 지 모르겠으면 위의 Post 위에 마우스 올리면 변수 설명 볼 수 있음
        
    # blog - views.py로 이동