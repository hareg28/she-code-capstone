from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):  
    STUDENT = 'student'
    ADMIN = 'admin'
    SUPER_ADMIN = 'super_admin'
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (ADMIN, 'Admin'),
        (SUPER_ADMIN, 'Super Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)

    def __str__(self):
        return self.username


class Book(models.Model):  
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('borrowed', 'Borrowed')])

    def __str__(self):
        return self.title


class Review(models.Model):  
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"


class BorrowedBook(models.Model):  
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"





