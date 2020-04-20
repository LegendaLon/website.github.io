from django.urls import path

from . import views

app_name = 'base'
urlpatterns = [
    path('', views.start_base, name = 'start_base'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('join', views.join_the_server, name = 'join'),
]