from django.contrib import admin
from blog.models.category import Category

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_title',)
	search_fields = ('category_title',)
	ordering = ('-id',)
	list_per_page = 5

admin.site.register(Category, CategoryAdmin)