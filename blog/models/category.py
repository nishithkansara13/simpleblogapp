from django.db import models

# Create your models here.
class Category(models.Model):
	category_title = models.CharField('Category Title', max_length=255)

	class Meta:
		ordering = ['-id']
		
	def __str__(self):
		return self.category_title