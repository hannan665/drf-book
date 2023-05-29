from django.db import models

from user.models import CustomUser


class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    published_at = models.DateField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_review')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')
    rating = models.PositiveIntegerField()
    feedback = models.TextField()

