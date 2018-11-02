from rest_framework import serializers
from .models import Author, Book


class AuthorListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "name": value.full_name,
            "id": value.id
        }


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())

    class Meta:
        model = Book
        exclude = ('created',)

    


class BookDetailSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='get_color_display')
    authors = AuthorListingField(many=True, read_only=True)

    class Meta:
        model = Book
        exclude = ('created',)


class AuthorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'imageUrl', 'books']


class AuthorDetailSerializer(serializers.ModelSerializer):
    books = BookDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'imageUrl', 'books']
