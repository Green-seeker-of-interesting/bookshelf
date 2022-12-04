from django.shortcuts import render

from web_client.models import Book

def index(request):
    ordering = request.GET.get('ord')
    books = Book.objects.all().order_by(ordering)
    return render(request ,"index.html", context={
        "books" : books,
    })