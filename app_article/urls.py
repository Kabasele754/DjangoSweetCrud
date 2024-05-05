from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/detail/<int:pk>/', views.show_article_details, name='article_detail'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/<int:pk>/update/', views.article_update, name='article_update'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
]
