from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, WishlistEntryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'wishlist', WishlistEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
