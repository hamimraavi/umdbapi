from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'([\w+ ]+)(?:/([0-9]+))$)', views.get_movie_results),
    url(r'^$', views.index, name='index'),
]
