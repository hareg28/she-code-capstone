from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('search_books/', views.search_books, name='search_books'),
    path('manage-books/', views.manage_books, name='manage_books'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
     path('profile/', views.user_profile, name='user_profile'),
]

