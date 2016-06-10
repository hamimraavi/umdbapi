import re
import search
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Welcome to UMDb!")


def get_movie_results(request):
    moviename = request.GET.get('t')
    res = search.get_all_movies(moviename)
    return JsonResponse(res, safe=False)


def get_movie_details(request, title_id):
    if title_id.endswith("/"):
        title_id = title_id[:-len("/")]
    validTitle = re.search(r'^tt[0-9]+$', title_id)
    if validTitle:
        res = search.get_all_details(title_id)
        return JsonResponse(res, safe=False)
    else:
        show_bad_request(request)


def show_bad_request(request):
    response = {}
    response["Error"] = "400"
    response["Message"] = "Bad Request"
    return JsonResponse(response)
