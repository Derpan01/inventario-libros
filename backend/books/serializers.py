from rest_framework import serializers
from .models import Book, WishlistEntry
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class WishlistEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistEntry
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
