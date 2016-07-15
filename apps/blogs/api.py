"""Api File for Blog."""

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Blog
from .serializer import BlogSerializer
from slugify import slugify


class BlogView(APIView):
    """List all Blogs, or create a new user."""

    def get(self, request, format=None):
        """Get method for serializer to view all Blog."""
        blogs = Blog.objects.all().order_by('created_at')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Post method for serializers to create new ppt. not tested."""
        print request.data
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            print 'here'
            serializer.save(request)
            response = {'success': True, 'data': serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            print 'or here'
            response = {'success': False, 'data': serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete method for BlogView."""
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogDetails(APIView):
    """Retrieve a Blog instance."""

    def get_object(self, pk):
        """Geting the object according to values."""
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Get method for UserDetails."""
        blog = self.get_object(pk)
        blog = BlogSerializer(blog)
        return Response(blog.data)


class SearchBlog(APIView):
    """Search a Blog instance by their title."""

    def get_object_list(self, title):
        """Geting the object according to values."""
        try:
            data = Blog.objects.filter(title__icontains=title)
            return data
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """Get method for serializers."""
        title = request.GET.get('title', None)
        blog = self.get_object_list(str(title))
        blog = BlogSerializer(blog, many=True)
        return Response(blog.data)
