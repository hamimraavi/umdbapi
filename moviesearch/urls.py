from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'.*$', views.get_movie_results),
    url(r'^$', views.index, name='index'),
]
