import json
import re
from BeautifulSoup import BeautifulSoup
from mechanize import Browser


def get_soup(movie, index):
    movie = '+'.join(movie.split())
    url = "%s%s%s" % (
        "http://www.imdb.com/find?ref_=nv_sr_fn&q=",
        movie,
        "&s=all"
    )
    br = Browser()
    br.open(url)
    try:
        link = list(br.links(url_regex=re.compile(r"/title/tt*")))[index]
    except:
        return ""
    else:
        res = br.follow_link(link)
        soup = BeautifulSoup(res.read())
        return soup


def get_title(movie, soup):
    try:
        return soup.find('title').contents[0]
    except:
        return "N/A"


def get_year(movie, soup):
    try:
        title_year = soup.find('span', id='titleYear')
        year = str(title_year)
        return re.search('.*([0-9]{4}).*', year).group(1)
    except:
        return "N/A"


def get_rating(movie, soup):
    try:
        rate = soup.find('span', itemprop='ratingValue')
        return str(rate.contents[0])
    except:
        return "N/A"


def get_votes(movie, soup):
    try:
        return soup.find('span', itemprop='ratingCount').contents[0]
    except:
        return "N/A"


def get_actors(movie, soup):
    try:
        actor_list = soup.findAll('span', itemprop='actors')
        actors = ""
        for actor in actor_list:
            str_act = str(actor).rpartition('itemprop="name"')[-1]
            actors += (re.search('\>(.*?)\<', str_act).group(1) + ", ")
        if actors.endswith(", "):
            actors = actors[:-len(", ")]
        return actors
    except:
        return "N/A"


def get_director(movie, soup):
    try:
        director_list = soup.findAll('span', itemprop='director')
        directors = ""
        for director in director_list:
            str_dir = str(director).rpartition('itemprop="name"')[-1]
            directors += (re.search('\>(.*?)\<', str_dir).group(1) + ", ")
        if directors.endswith(", "):
            directors = directors[:-len(", ")]
        return directors
    except:
        return "N/A"


def get_writer(movie, soup):
    try:
        writer_list = soup.findAll('span', itemprop='creator')
        writers = ""
        for writer in writer_list:
            str_writer = str(writer).rpartition('itemprop="name"')[-1]
            writers += (re.search('\>(.*?)\<', str_writer).group(1) + ", ")
        if writers.endswith(", "):
            writers = writers[:-len(", ")]
        return writers
    except:
        return "N/A"


def get_duration(movie, soup):
    try:
        return soup.find('time', itemprop='duration').contents[0].strip()
    except:
        return "N/A"


def get_content_rating(movie, soup):
    try:
        rate = soup.find('span', itemprop='contentRating').contents[0].strip()
        print rate
        return rate
    except:
        return "N/A"


def get_genre(movie, soup):
    try:
        genre_list = soup.findAll('span', itemprop='genre')
        genres = ""
        for genre in genre_list:
            str_gen = str(genre).rpartition('itemprop="genre"')[-1]
            genres += (re.search('\>(.*?)\<', str_gen).group(1) + ", ")
        if genres.endswith(", "):
            genres = genres[:-len(", ")]
        return genres
    except:
        return "N/A"


def get_release_date(movie, soup):
    try:
        date = soup.find('meta', itemprop='datePublished').contents[0]
        return date
    except:
        return "N/A"


def get_all_details(movie, index):
    response = {}

    soup = get_soup(movie, index)

    title = get_title(movie, soup)
    if title == "N/A":
        movie_response = "False"
        error_code = "404"
        response["Response"] = movie_response
        response["Error"] = error_code
        return json.dumps(response)

    year = get_year(movie, soup)
    rating = get_rating(movie, soup)
    votes = get_votes(movie, soup)
    duration = get_duration(movie, soup)
    content = get_content_rating(movie, soup)
    genre = get_genre(movie, soup)
    director = get_director(movie, soup)
    writer = get_writer(movie, soup)
    actors = get_actors(movie, soup)

    response["Title"] = title
    response["Year"] = year
    response["IMDb Rating"] = rating
    response["Votes"] = votes
    response["Runtime"] = duration
    response["Rated"] = content
    response["Genre"] = genre
    response['Director'] = director
    response['Writer'] = writer
    response['Actors'] = actors
    return JsonResponse(response)


def everything(movie): 
    k1 = get_all_details(movie, 0)
    k2 = get_all_details(movie, 2)
    k3 = get_all_details(movie, 4)
    ans = []
    ans.append(k1)
    ans.append(k2)
    ans.append(k3)
    return JsonResponse(ans, safe=False)
