from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(["POST"])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if not username or not password:
        return Response({"error": "Username and password required."}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({"message": "User created successfully."}, status=201)

# backend/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, BookViewSet, WishlistEntryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'wishlist', WishlistEntryViewSet, basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
]