"""Serializers for presentation and profile."""
from rest_framework import serializers
from .models import Blog
from usermanager.serializers import UserSerializer


class BlogSerializer(serializers.ModelSerializer):
    """Main Serializer for Presentation Model."""

    creator = UserSerializer(many=False, read_only=True)

    class Meta:
        """Meta class for the serializer."""

        model = Blog
        fields = ('id', 'title', 'thumbnail', 'slug',
                  'creator', 'body', 'created_at')
