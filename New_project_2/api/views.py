from django.shortcuts import render
from api.models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        "title": "DJANGO API",
        "books": books
    }
    return render(request, "api/index.html", context)


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "title": "Detail Book",
        "book": book
    }
    return render(request, "api/detail.html", context)
