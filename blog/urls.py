from django.urls import path, include

#from multimedia.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]