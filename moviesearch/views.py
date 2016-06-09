import search
from django.http import JsonResponse


def index(request):
    res = search.get_all_details("inception")
    return HttpResponse(res)


def results(request):
    moviename = request.GET['t']
    res = search.everything(moviename)
    return JsonResponse(res, safe=False)
