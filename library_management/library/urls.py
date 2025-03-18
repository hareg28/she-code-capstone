
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  
    path('search_book/', views.search_books, name='search_books'),
    path('manage_books/', views.manage_books, name='manage_books'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('add_book/', views.add_book, name='add_book'),
     path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('view_book/<int:book_id>/', views.view_book, name='view_book'),
    path('book_list/', views.book_list, name='book_list'), 

]

