from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('articles/', views.articles, name='blog-articles'),
    path('articles/<string>', views.articles, name='blog-articles'),
    path('articles/blog-post/', views.blog_post, name='blog-post'),
    path('articles/blog-post/<int:pk>', views.blog_post, name='blog-post'),
    path('about/', views.about, name='blog-about'),
]
