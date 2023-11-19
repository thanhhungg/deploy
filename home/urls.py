from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="home"),
    path('users/', views.CreateUserView.as_view(), name='create_user'),
    path('user/', views.user_list, name='user_list'),
    path('user_login/', views.LoginView.as_view(), name='login_view'),
    # path('receive/', views.receive_sensor_data, name="receive"),
    path('update_parkinglot/', views.update_parkinglot.as_view(), name="update_parkinglot"),
]
