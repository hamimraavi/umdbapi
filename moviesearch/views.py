import search
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Welcome to UMDb!")


def get_movie_results(request, moviename):
    #moviename = request.GET['t']
    #no_of_queries = request.GET['q']
    #res = search.get_all_movies(moviename, no_of_queries)
    return HttpResponse(moviename)
    #return JsonResponse(res, safe=False)
