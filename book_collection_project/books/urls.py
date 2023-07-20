from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView,BookRetrieveView, BookPartialUpdateView
from .views import book_list

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', BookRetrieveView.as_view(), name='book-retrieve'),
    path('books/<int:pk>/partial-update/', BookPartialUpdateView.as_view(), name='book-partial-update'), 
    
]



