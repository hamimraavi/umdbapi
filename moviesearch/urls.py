from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'search/.*$', views.get_movie_results),
    url(r'^$', views.index),
]
