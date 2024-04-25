from rest_framework import serializers
from .models import Quote, Author, Source, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'occupation']

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'source_text', 'source_type', 'date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image']

class QuoteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    source = SourceSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Quote
        fields = ['id', 'quote_text', 'quote_audio', 'image', 'author', 'source', 'category', 'created_at']
        extra_kwargs = {'quote_text': {'required': True}}
