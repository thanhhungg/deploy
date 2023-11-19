from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="home"),
    path('users/', views.CreateUserView.as_view(), name='create_user'),
    path('user/', views.user_list, name='user_list')
]
