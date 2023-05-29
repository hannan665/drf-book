from rest_framework import serializers

from book.models import Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)
    user_email = serializers.CharField(source="user.email", read_only=True)
    rating = serializers.IntegerField(max_value=7, min_value=1)

    class Meta:
        model = Review
        fields = ('id', 'rating', 'book', 'user_name', 'user_email', 'feedback')


class BookSerializer(serializers.ModelSerializer):
    book_review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ("id", "title", "author", 'content', 'published_at', 'price', 'quantity', 'book_review')
