from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task
from rest_framework.decorators import api_view, parser_classes

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the todo index.")

def task(request):
	context = {}
	# template = loader.get_template('todo/task.html')
	# return HttpResponse(template.render(context, request))
	return render(request, 'todo/task.html', context)