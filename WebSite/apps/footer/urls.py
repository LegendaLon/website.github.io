from django.urls import path

from . import views

app_name = 'footer'
urlpatterns = [
    path('about', views.about, name = 'about'),
]