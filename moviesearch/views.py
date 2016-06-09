import search
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Welcome to UMDb!")


def get_movie_results(request, moviename, no_of_queries=1):
    #moviename = request.GET['t']
    #no_of_queries = request.GET['q']
    #res = search.get_all_movies(moviename, no_of_queries)
    return HttpResponse(no_of_queries)
    #return JsonResponse(res, safe=False)
