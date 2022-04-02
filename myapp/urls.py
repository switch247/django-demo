from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('todos/', views.todos, name='todos'),
    path('', views.home, name='home'),
]
