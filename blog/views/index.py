from django.shortcuts import render
from django.http import HttpResponse
from blog.models.blog import Blog
from blog.models.category import Category
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	categories = get_category_list()
	get_category_id = request.GET.get('category')
	get_search = request.GET.get('search')
	blogs = get_blog_list(get_category_id, get_search)
	paginator = Paginator(blogs, 2)
	page = request.GET.get('page')
	blogs = paginator.get_page(page)

	return render(request, 'blog/index.html', {'blogs':blogs, 'categories':categories, 'page':page, 'search':get_search, 'category':get_category_id,'default_image':str(settings.MEDIA_URL) + str(settings.DEFAULT_USER_IMAGE)})

def blog_detail(request, id):
	categories = get_category_list()
	blog = get_object_or_404(Blog, pk=id)
	return render(request, 'blog/single.html', {'blog':blog, 'categories':categories, 'default_image':str(settings.MEDIA_URL) + str(settings.DEFAULT_USER_IMAGE)})

def get_blog_list(category=None, search=None):
	blogs = Blog.objects.all().filter(blog_status = 'Active')
	if category and not search:
		blogs = blogs.filter(blog_category__id = category)
	elif not category and search:
		blogs = blogs.filter(Q(blog_title__icontains=str(search)) | Q(blog_content__icontains=str(search)) | Q(blog_category__category_title__icontains=str(search)) | Q(blog_user__username__icontains=str(search)) | Q(blog_user__first_name__icontains=str(search)) | Q(blog_user__last_name__icontains=str(search)))
	elif category and search:
		blogs = blogs.filter(Q(blog_category__id = category) & (Q(blog_title__icontains=str(search)) | Q(blog_content__icontains=str(search)) | Q(blog_category__category_title__icontains=str(search)) | Q(blog_user__username__icontains=str(search)) | Q(blog_user__first_name__icontains=str(search)) | Q(blog_user__last_name__icontains=str(search))))

	return blogs

def get_category_list():
	category = Category.objects.all() 
	return category