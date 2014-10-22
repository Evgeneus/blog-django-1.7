from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def basic_one(request):
	view = "basic_one"
	html = "<html><body>This is %s </body></html>" % view
	return HttpResponse(html)

def template_two(request):
	view = "template_two"
	t = get_template('myviews.html')
	html = t.render(Context({'name': view}))
	return HttpResponse(html)