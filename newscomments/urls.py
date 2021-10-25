from django.urls import path
from . import views

urlpatterns = [
    #views.index라는 뷰를 호출
    path('', views.index, name='index'),
    
    #views.add_comment라는 뷰를 호출
    path('add', views.add_comment, name='add_comment'),
]
