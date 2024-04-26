from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Author, Source, Category, Quote



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'occupation']
        
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'text', 'media', 'date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description']
        
class QuoteSerializer(serializers.ModelSerializer):
    audio = serializers.FileField(max_length=None, allow_empty_file=True, use_url=True)
    source = SourceSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Quote
        fields = ['id', 'title', 'content', 'created_at', 'audio', 'author', 'source', 'category']
        extra_kwargs = {
            'source': {'read_only': True},
            'category': {'read_only': True}
            # Remove 'author' from extra_kwargs since it's now just a CharField
        }

    def create(self, validated_data):
        # Assuming you're creating a quote without nested objects or they are passed as IDs.
        return Quote.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Manually handle the assignment of each field to support nested objects or direct attributes.
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.audio = validated_data.get('audio', instance.audio)
        # Further fields can be updated similarly
        instance.save()
        return instance
        
