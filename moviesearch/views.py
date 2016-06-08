from django.http import HttpResponse
import search


def index(request):
    res = search.get_all_details("inception")
    return HttpResponse(res)


def results1(request):
    moviename = request.GET['t']
    res = search.get_all_details(moviename)
    return HttpResponse(res)

# Create your views here.
