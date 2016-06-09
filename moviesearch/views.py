import search
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Welcome to UMDb!")


def get_movie_results(request, moviename, no_of_queries=1):
    res = search.get_all_movies(moviename, no_of_queries)
    return JsonResponse(res, safe=False)


def show_bad_request(request):
    response = {}
    response["Error: "] = 400
    response["Message: "] = "Bad Request"
    return JsonResponse(response)
