from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^moviesearch/([a-z]+)/$', views.results, name='results'),
    url(r'.*$', views.results1),
    url(r'^$', views.index, name='index'),
]
