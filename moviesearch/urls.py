from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^([\w ]+)/$', views.get_movie_results),
    url(r'^([\w ]+)/([\d]+)/$', views.get_movie_results),
    url(r'^$', views.index, name='index'),
]
