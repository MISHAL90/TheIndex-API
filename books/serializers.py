from rest_framework import serializers
from .models import Author, Book
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)
        validated_data['token'] = token
        return validated_data


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
