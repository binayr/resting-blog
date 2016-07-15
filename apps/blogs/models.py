from __future__ import unicode_literals
import os
import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
def get_file_path(instance, filename):
    if instance:
        return os.path.join("static", 'uploads', str(instance.slug), filename)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.FileField(upload_to=get_file_path, null=True, blank=True)
    creator = models.ForeignKey(User)
    body = models.CharField(max_length=5000)
    slug = models.SlugField(max_length=50)
    created_at = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return self.title
