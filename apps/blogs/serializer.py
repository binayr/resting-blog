"""Serializers for presentation and profile."""
from rest_framework import serializers
from .models import Blog
from usermanager.serializers import UserSerializer
from slugify import slugify


class BlogSerializer(serializers.ModelSerializer):
    """Main Serializer for Presentation Model."""

    creator = UserSerializer(many=False, read_only=True)

    class Meta:
        """Meta class for the serializer."""

        model = Blog
        fields = ('id', 'title', 'thumbnail', 'slug',
                  'creator', 'body', 'created_at')

    def save(self, request, *args, **kwargs):
        blog = Blog.objects.create(
            title=self.data['title'], body=self.data['body'],
            slug=slugify(self.data['slug']), creator=request.user)
        return blog
