from django.contrib import admin

from .models import Post, PostFile, PostImage, PostType

# Register your models here.

admin.site.register(Post)
admin.site.register(PostFile)
admin.site.register(PostImage)
admin.site.register(PostType)

# 관리자사이트에서 객체 생성 (id: admin, pw: qwerasdf)
# 카테고리 2가지 만들기
# 글 카테고리별 2개
# 이미지, 첨부파일 자유 -> 이미지 및 첨부파일을 올리고 src 폴더 눌러 F5 누르면 files가 생겨 여기에 들어감(media_root)
# 그 아래 폴더들이 upload_to임.

# blog - forms.py로 이동
