import time

from rest_framework import viewsets, mixins, serializers

from .models import Author, Book
from .serializers import AuthorListSerializer, AuthorDetailSerializer, BookSerializer, BookDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed
    """
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed
    """
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorListSerializer
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorDetailSerializer
