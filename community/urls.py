from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'), # 게시글 전체 보기
    path('create_article/', views.create_article, name='create_article'), # 게시글 작성
    path('<int:article_id>/', views.article_detail, name='article_detail'), #게시글 상세
    path('<int:article_id>/update_article/', views.update_article, name='update_article'), # 게시글 수정
    path('<int:article_id>/delete_article/', views.delete_article, name='delete_article'), # 게시글 삭제
]