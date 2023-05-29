from rest_framework import filters, mixins, permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from book.models import Book, Review
from book.serializers import BookSerializer, ReviewSerializer


class GetBooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'author']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('book_review__user')
        return queryset


class CreateReviewViewSet(
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
