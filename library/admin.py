from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Review, BorrowedBook
from .models import Book

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(BorrowedBook)

