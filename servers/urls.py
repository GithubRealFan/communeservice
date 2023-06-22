from django.urls import path
from . import views

# /servers
# /servers/1/detail
# /servers/new

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]