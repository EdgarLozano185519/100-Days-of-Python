from django.shortcuts import render
from .models import Book

# Create your views here.


def home(request):
    all_books = Book.objects.all()
    return render(request, "book_store/index.html", {"books": all_books})


def details(request, book_title):
    book_to_find = Book.objects.get(title=book_title)
    return render(request, "book_store/details.html", {
        "title": book_to_find.title,
        "book_author": book_to_find.author,
        "book_rating": book_to_find.rating,
        "book_is_best_seller": book_to_find.is_best_seller
    })
