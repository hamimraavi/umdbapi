import search
from django.http import HttpResponse


def index(request):
    res = search.get_all_details("inception")
    return HttpResponse(res)


def results(request):
    moviename = request.GET['t']
    res = search.get_all_details(moviename)
    return HttpResponse(res)
