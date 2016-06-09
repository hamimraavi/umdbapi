from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'([\w ]+)/(?P<no_of_queries>[\d]+)$', views.get_movie_results),
    url(r'^$', views.index, name='index'),
]
