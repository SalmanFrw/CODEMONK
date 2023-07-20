

# Create your models here.

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()
    # Add other fields as needed



    def __str__(self):
        return self.title  # Return the book's title as the string representation
