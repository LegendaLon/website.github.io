from django.urls import path

from . import views

app_name = 'coolstory'
urlpatterns = [
    path('', views.start_story, name = 'start_story'),
	path('<int:post_id>/', views.detail_story, name='detail_story'),
]