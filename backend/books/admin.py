from django.contrib import admin
from .models import Book, WishlistEntry

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'edition', 'cover_type', 'owner')
    search_fields = ('title', 'author')
    list_filter = ('cover_type',)

@admin.register(WishlistEntry)
class WishlistEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'owned')
    list_filter = ('owned', 'user')
    search_fields = ('book__title', 'user__username')
