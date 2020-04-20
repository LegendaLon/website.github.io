from django.shortcuts import render
from django.http import Http404

from .models import Post, join_info

def start_base(request):
	post = Post.objects.order_by('-id')
	return render(request, 'base/templates_base.html', locals())

def detail(request, post_id):
	try:
		a = Post.objects.get(id = post_id)
	except:
		raise Http404("Данный пост не найден! =(")
	return render(request, 'base/templates_detail.html', {'post': a})

def join_the_server(request):
	info = join_info.objects.order_by('-id')
	return render(request, 'base/templates_join.html', locals())