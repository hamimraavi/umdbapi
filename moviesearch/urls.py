from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'.*$', views.results1),
    url(r'^$', views.index, name='index'),
]
