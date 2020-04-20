from django.shortcuts import render

# Все функции

def about(request):
	return render(request, 'footer/about.html')