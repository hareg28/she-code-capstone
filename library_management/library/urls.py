from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
     path('search/', views.search_books, name='search_books'),
    path('manage-books/', views.manage_books, name='manage_books'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]