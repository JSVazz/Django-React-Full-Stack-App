from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Source(models.Model):
    source_text = models.CharField(max_length=200)
    source_type = models.CharField(max_length=100)  # Consider choices or a separate model if many types
    date = models.CharField(max_length=100)  # Or models.DateField() if actual dates are used

    def __str__(self):
        return self.source_text

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.title

class Quote(models.Model):
    quote_text = models.TextField()
    quote_audio = models.FileField(upload_to='quotes/audio/', blank=True, null=True)
    image = models.ImageField(upload_to='quotes/images/', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="quotes")
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="quotes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quotes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quote_text[:50]}..."  # Show first 50 characters

