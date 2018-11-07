import time
from rest_framework.response import Response
from rest_framework import viewsets, mixins, serializers
from rest_framework.generics import CreateAPIView


from .models import Author, Book
from .serializers import AuthorListSerializer, AuthorDetailSerializer, BookSerializer, BookDetailSerializer, UserCreateSerializer

from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed
    """
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            book = Book.objects.create(
                title = valid_data['title'],
                color = valid_data['color']
                )
            book.authors.set(valid_data['authors'])
            book.save()
            book_json = BookDetailSerializer(book).data
            return Response(book_json)
        return Response(serializer.errors)

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed
    """
    queryset = Author.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorListSerializer
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorListSerializer
