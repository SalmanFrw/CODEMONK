# books/serializers.py




from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        # Add validation logic for the title field (example: length validation)
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_author(self, value):
        # Add validation logic for the author field (example: format validation)
        if not value.isalpha():
            raise serializers.ValidationError("Author name must contain only alphabetic characters.")
        return value

    # Add similar validate methods for other fields as needed.
