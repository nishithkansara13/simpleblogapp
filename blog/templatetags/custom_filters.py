from django import template

register = template.Library()

@register.filter
def get_n_characters(value):
	full_str = str(value)
	return full_str[0:100] + str('...')