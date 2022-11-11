from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'), # 게시글 전체 보기
    path('create_article/', views.create_article, name='create_article'), # 게시글 작성
]