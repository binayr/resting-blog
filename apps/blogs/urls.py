from django.conf.urls import patterns, include, url
from . import api
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^blogs/new/$', views.NewBlogView.as_view(),
        name="add_new_blog"),
    url(r'^blogs/all/$', views.BlogView.as_view(),
        name="all_prezi"),
    url(r'^presentation-summary/$', views.get_blog_summary,
        name="get_blog_summary"),

    # API URLs
    url(r'^api/v1/blogs/$', api.BlogView.as_view(),
        name="blogs_api"),
    url(r'^api/v1/blog/(?P<pk>[-\w]+)/',
        api.BlogDetails.as_view(), name="blog_api"),
    url(r'^api/v1/search/blog/',
        api.SearchBlog.as_view(), name="search_blog_api"),
)
