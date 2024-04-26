
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import QuoteSerializer, AuthorSerializer, SourceSerializer, CategorySerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Quote, Author, Source, Category


class QuoteListCreate(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Example: filtering by author name passed as a query parameter
        author_name = self.request.query_params.get('author', None)
        if author_name:
            return Quote.objects.filter(author=author_name)
        return Quote.objects.all()

    def perform_create(self, serializer):
    # Assuming `author_name` is sent as part of the request
        author_name = self.request.data.get('author', None)
        if author_name:
            serializer.save(author=author_name)
        else:
            # Handle the case where no author name is provided
            raise ValidationError("Author name is required.")



class QuoteDelete(generics.DestroyAPIView):
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Quote.objects.filter(author=user)

class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Quote.objects.filter(author=self.request.user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

class SourceListCreate(generics.ListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

