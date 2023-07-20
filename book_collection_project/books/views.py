from django.shortcuts import render

# Create your views here.

# books/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.routers import DefaultRouter



class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    

class BookPartialUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def partial_update(self, request, *args, **kwargs):
    book_id = self.kwargs['pk']  # Access the book ID from kwargs
    # Perform partial update using the book_id and request.data
    # Your implementation for partial update here...




def index(request):
    return HttpResponse("Welcome to the Book Collection API.")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})



