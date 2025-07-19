from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Book, WishlistEntry
from .serializers import BookSerializer, WishlistEntrySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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
