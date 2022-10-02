from django.urls import path
from main import views


urlpatterns = [
    path('', views.index),
    path('articles/<int:pk>', views.article),
    path('articles/new', views.create_article),
    path('author/<int:pk>', views.author),
]