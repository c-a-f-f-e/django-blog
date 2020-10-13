from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), # 追加
    path('post/new/', views.CreatePostView.as_view(), name='post_new'), # 追加
]

class XXXXX(View):
    def get(self, request, *args, **kwargs):
        # 表示したら必ず最初に呼ばれる
    def post(self, request, *args, **kwargs):
        # 画面で送信ボタンなど、submitされた時に呼ばれる