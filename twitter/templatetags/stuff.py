from django import template, Context
register = template.Library()

@register.simple_tag
def stuff():
	hi = "hi"
	return hi
	
	
print "hello"