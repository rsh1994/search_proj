from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render
from haystack.query import SearchQuerySet

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def search(request):
    query = request.GET.get('q', '')
    results = SearchQuerySet().models(Book).filter(content=query) if query else []
    return render(request, 'search_app/search.html', {'results': results, 'query': query})