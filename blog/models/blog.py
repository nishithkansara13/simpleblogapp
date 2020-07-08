from django.db import models
from django.contrib.auth.models import User
from blog.models.category import Category
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

# Create your models here.
@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

class Blog(models.Model):
	INACTIVE='Inactive'
	ACTIVE='Active'
	STATUS_CHOICES=((INACTIVE, 'Inactive'),(ACTIVE, 'Active'))

	blog_title = models.CharField('Blog Title', max_length=255)
	blog_category = models.ForeignKey(Category, on_delete=models.CASCADE)
	blog_user = models.ForeignKey(User, on_delete=models.CASCADE)
	blog_image = models.ImageField('Blog Image', upload_to=PathAndRename(''), blank=True)
	blog_content = models.TextField()
	blog_status = models.CharField('Status', max_length=8, choices=STATUS_CHOICES, default=ACTIVE)
	blog_created_date = models.DateTimeField(auto_now_add=True)
	blog_updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-id']
		
	def __str__(self):
		return self.blog_title