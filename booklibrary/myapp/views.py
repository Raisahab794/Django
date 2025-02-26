from django.shortcuts import render

# Hardcoded list of books
books = [
    {"title": "Book One", "author": "Author A", "year": 2020},
    {"title": "Book Two", "author": "Author B", "year": 2021},
    {"title": "Book Three", "author": "Author A", "year": 2022},
    {"title": "Book Four", "author": "Author C", "year": 2020},
]

def library(request, author=None, year=None):
    filtered_books = books
    if author:
        filtered_books = [book for book in filtered_books if book["author"].lower() == author.lower()]
    if year:
        filtered_books = [book for book in filtered_books if book["year"] == int(year)]
    
    context = {
        "books": filtered_books,
        "filter_author": author,
        "filter_year": year,
    }
    return render(request, "library.html", context)

def custom_404(request, exception):
    return render(request, '404.html', status=404)
