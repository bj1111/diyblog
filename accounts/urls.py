from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user-info/<str:user_id>', views.user_info, name='user_info'),
    path('user-info/<str:user_id>/reset-password/', views.reset_password, name='reset_password'),
]