from django.shortcuts import render
from django.http import Http404
# from django.views.generic.list import ListView, DetailView
from django.views import View

from .models import *

def start_story(request):
	person = Person.objects.order_by('-id')
	return render(request, 'coolstory/templates_base.html', {'person': person})

def detail_story(request, post_id):
	try:
		person = Person.objects.get(id = post_id)
		x = person.history.order_by('-id')
	except:
		raise Http404("Данный персонаж не найден! =(")

	return render(request, 'coolstory/templates_person.html', {'x': x})