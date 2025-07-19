from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Book, WishlistEntry
from .serializers import BookSerializer, WishlistEntrySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register_user(request):
    try:
        username = request.data['username']
        password = make_password(request.data['password'])
        email = request.data.get('email', '')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, password=password, email=email)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

    except KeyError:
        return Response({'error': 'Missing username or password'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class WishlistEntryViewSet(viewsets.ModelViewSet):
    queryset = WishlistEntry.objects.none()  # ← Add this line
    serializer_class = WishlistEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WishlistEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
