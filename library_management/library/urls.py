from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
     path('search/', views.search_books, name='search_books'),
    path('manage-books/', views.manage_books, name='manage_books'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('add-book/', views.add_book, name='add_book'),
     path('update-book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('view-book/<int:book_id>/', views.view_book, name='view_book'),

]