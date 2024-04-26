from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Source(models.Model):
    text = models.CharField(max_length=200)  # Description of the source
    media = models.CharField(max_length=100)  # Type of source, e.g., Movie, Book, Website
    date = models.DateField()  # The date of the source publication or creation

    def __str__(self):
        return f"{self.text} ({self.media})"

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Quote(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default='Unknown Author')  # Provide a default value
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    source = models.ForeignKey('Source', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    



