from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/<int:blog_id>/', views.detail, name='detail'),
    path('blogs/user_blog/', views.user_blog, name='user_blog'),
    path('blogs/', views.list, name='list'),
    path('blogs/create/', views.create, name='create'),
    path('blogs/update/<int:blog_id>/', views.update, name='update'),
    path('blogs/delete/<int:blog_id>/', views.delete, name='delete'),
]
