from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    COVER_CHOICES = [
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    edition = models.CharField(max_length=100, blank=True)
    cover_type = models.CharField(max_length=10, choices=COVER_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True, blank=True)

    def __str__(self):
        return self.title

class WishlistEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    owned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} wants {self.book.title}"
