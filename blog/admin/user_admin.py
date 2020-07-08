from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

# Create your models here.
class CustomUserAdmin(UserAdmin):
	def get_fieldsets(self, request, obj=None):
		if not obj:
			return self.add_fieldsets
		fieldset = super().get_fieldsets(request, obj)	
		if request.user.groups.all().filter(name='Blog User').exists():
			fieldset = ((None, {'fields': ('username', 'password')}),(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),)
		return fieldset
	def get_queryset(self, request):
		default_user_list = super(CustomUserAdmin, self).get_queryset(request)
		if request.user.groups.all().filter(name='Blog User').exists():
			return default_user_list.filter(id=request.user.id)
		return default_user_list

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)