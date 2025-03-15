from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from .models import Book, User  # Import the Book and User models
from .forms import RegistrationForm  # Import the RegistrationForm
from django.shortcuts import get_object_or_404
from .forms import BookForm
from .forms import UserForm

def is_admin(user):
    return user.role == User.ADMIN or user.role == User.SUPER_ADMIN
def user_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'user_profile.html', {'form': form})
@user_passes_test(is_admin)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def search_books(request):
    query = request.GET.get('q', '')  # Get search query from request
    books = Book.objects.none()  # Default empty queryset

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query) | 
            Q(genre__icontains=query)
        )
        return render(request, 'book_list.html', {'books': books, 'query': query})
"""def search_books(request):
    query = request.GET.get('query','')  # Get the search query from the URL
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__icontains=query))
        return render(request,'books_list.html')
    return render(request, 'home.html', {'books': books})"""


@user_passes_test(is_admin)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('manage_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

@user_passes_test(is_admin)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('manage_books')
    return render(request, 'delete_book.html', {'book': book})
def is_admin(user):
    return user.role == User.ADMIN or user.role == User.SUPER_ADMIN

@user_passes_test(is_admin)
def manage_books(request):
    # Book management logic
    books = Book.objects.all()  # Example: Retrieve all books
    return render(request, 'manage_books.html', {'books': books})

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')







