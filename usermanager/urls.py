from django.conf.urls import include, url
from django.contrib import admin
from . import views
from . import api

urlpatterns = [
    # Examples:

    url(r'^admin/', include(admin.site.urls)),

    # Api Urls
    url(r'^api/users/', api.UserList.as_view(), name="user_api"),
    url(r'^api/user/(?P<term>[-\w]+)/', api.UserQuery.as_view(), name="userdetails_api"),
]
