from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, WishlistEntryViewSet, RegisterView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'wishlist', WishlistEntryViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # ✅ Keep this
    path('', include(router.urls)),                              # ✅ and this
]
