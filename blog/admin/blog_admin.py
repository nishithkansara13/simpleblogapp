from django.contrib import admin
from blog.models.blog import Blog
from django.conf import settings
from django.utils.safestring import mark_safe
import os

class BlogAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		default_blog_list = super(BlogAdmin, self).get_queryset(request)
		if request.user.groups.all().filter(name='Blog User').exists():
			return default_blog_list.filter(blog_user=request.user)
		return default_blog_list

	def blog_image_previw(self, obj):
		img_url = obj.blog_image.url if obj.blog_image else os.path.join(settings.MEDIA_URL, settings.DEFAULT_USER_IMAGE)
		return mark_safe('<img src="{url}" width="125" height="140" />'.format(url = img_url))

	def blog_picture(self, obj):
		img_url = obj.blog_image.url if obj.blog_image else os.path.join(settings.MEDIA_URL, settings.DEFAULT_USER_IMAGE)
		return mark_safe('<img src="{url}" width="45" height="45" />'.format(url = img_url))

	def mark_active(modeladmin, request, queryset):
		queryset.update(blog_status='Active')
	mark_active.short_description = "Mark selected as Active"

	def mark_inactive(modeladmin, request, queryset):
		queryset.update(blog_status='Inactive')
	mark_inactive.short_description = "Mark selected as Inactive"

	list_display = ('blog_picture', 'blog_title','blog_category', 'blog_user', 'blog_status', 'blog_created_date', 'blog_updated_date')
	search_fields = ('blog_title', 'blog_user__username')
	list_filter = ('blog_category','blog_status',)
	readonly_fields= ['blog_created_date', 'blog_updated_date', 'blog_image_previw']
	fieldsets = ((None, {'fields': ('blog_title', 'blog_category', 'blog_user', 'blog_image','blog_image_previw', 'blog_content', 'blog_status', 'blog_created_date', 'blog_updated_date')}),)
	list_display_links = ('blog_picture', 'blog_title')
	actions = [mark_active, mark_inactive]
	ordering = ('-id',)
	list_per_page = 10

admin.site.register(Blog, BlogAdmin)