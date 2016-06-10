import re

from BeautifulSoup import BeautifulSoup
from mechanize import Browser

FIELD_NOT_FOUND = "N/A"


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
        link = list(br.links(url_regex=re.compile(r"/title/tt*")))[index*2]
    except AttributeError:
        return ""
    else:
        res = br.follow_link(link)
        soup = BeautifulSoup(res.read())
        return soup


def get_title_id(movie, index):
    movie = '+'.join(movie.split())
    url = "%s%s%s" % (
        "http://www.imdb.com/find?ref_=nv_sr_fn&q=",
        movie,
        "&s=all"
    )
    br = Browser()
    br.open(url)
    try:
        link = list(br.links(url_regex=re.compile(r"/title/tt*")))[index*2]
    except AttributeError:
        return ""
    else:
        title_id = re.search(r"tt[0-9]+", str(link)).group()
        return title_id


def get_title(soup):
    try:
        return soup.find('title').contents[0].replace(" - IMDb", "")
    except AttributeError:
        return FIELD_NOT_FOUND


def get_year(soup):
    try:
        title_year = str(soup.find('span', id='titleYear'))
        return re.search('.*([0-9]{4}).*', title_year).group(1)
    except AttributeError:
        return FIELD_NOT_FOUND


def get_rating(soup):
    try:
        rate = soup.find('span', itemprop='ratingValue')
        return str(rate.contents[0])
    except AttributeError:
        return FIELD_NOT_FOUND


def get_votes(soup):
    try:
        return soup.find('span', itemprop='ratingCount').contents[0]
    except AttributeError:
        return FIELD_NOT_FOUND


def get_actors(soup):
    try:
        actor_list = soup.findAll('span', itemprop='actors')
    except AttributeError:
        return FIELD_NOT_FOUND
    else:
        actors = ""
        for actor in actor_list:
            str_act = str(actor).rpartition('itemprop="name"')[-1]
            actors += (re.search('\>(.*?)\<', str_act).group(1) + ", ")
        if actors.endswith(", "):
            actors = actors[:-len(", ")]
        return actors


def get_director(soup):
    try:
        director_list = soup.findAll('span', itemprop='director')
    except AttributeError:
        return FIELD_NOT_FOUND
    else:
        directors = ""
        for director in director_list:
            str_dir = str(director).rpartition('itemprop="name"')[-1]
            directors += (re.search('\>(.*?)\<', str_dir).group(1) + ", ")
        if directors.endswith(", "):
            directors = directors[:-len(", ")]
        return directors


def get_writer(soup):
    try:
        writer_list = soup.findAll('span', itemprop='creator')
    except AttributeError:
        return FIELD_NOT_FOUND
    else:
        writers = ""
        for writer in writer_list:
            str_writer = str(writer).rpartition('itemprop="name"')[-1]
            writers += (re.search('\>(.*?)\<', str_writer).group(1) + ", ")
        if writers.endswith(", "):
            writers = writers[:-len(", ")]
        return writers


def get_duration(soup):
    try:
        return soup.find('time', itemprop='duration').contents[0].strip()
    except AttributeError:
        return FIELD_NOT_FOUND


def get_content_rating(soup):
    try:
        rate = soup.find('span', itemprop='contentRating').contents[0].strip()
        return rate
    except AttributeError:
        return FIELD_NOT_FOUND


def get_genre(soup):
    try:
        genre_list = soup.findAll('span', itemprop='genre')
    except AttributeError:
        return FIELD_NOT_FOUND
    else:
        genres = ""
        for genre in genre_list:
            str_gen = str(genre).rpartition('itemprop="genre"')[-1]
            genres += (re.search('\>(.*?)\<', str_gen).group(1) + ", ")
        if genres.endswith(", "):
            genres = genres[:-len(", ")]
        return genres


def get_release_date(soup):
    try:
        date = soup.find('meta', itemprop='datePublished').contents[0]
        return date
    except AttributeError:
        return FIELD_NOT_FOUND


def get_all_details(title_id):
    response = {}
    url = "%s%s%s" % (
        "http://www.imdb.com/title/",
        title_id,
        "/?ref_=fn_al_tt_1"
    )

    br = Browser()
    res = br.open(url)

    soup = BeautifulSoup(res)
    title = get_title(soup)
    if title == FIELD_NOT_FOUND:
        response["Error"] = "404"
        response["Message"] = "Not found"
        return response

    year = get_year(soup)
    rating = get_rating(soup)
    votes = get_votes(soup)
    duration = get_duration(soup)
    content = get_content_rating(soup)
    genre = get_genre(soup)
    director = get_director(soup)
    writer = get_writer(soup)
    actors = get_actors(soup)

    response["Title"] = title
    response["Year"] = year
    response["IMDb Rating"] = rating
    response["Votes"] = votes
    response["Runtime"] = duration
    response["Rated"] = content
    response["Genre"] = genre
    response["Director"] = director
    response["Writer"] = writer
    response["Actors"] = actors
    return response


def get_search_results(movie, index):
    response = {}

    soup = get_soup(movie, index)

    title = get_title(soup)
    if title == FIELD_NOT_FOUND:
        return response

    title_id = get_title_id(movie, index)
    rating = get_rating(soup)
    actors = get_actors(soup)

    response["Title"] = title
    response["Title ID"] = title_id
    response["IMDb Rating"] = rating
    response["Actors"] = actors
    return response


def get_all_movies(moviename):
    all_movies = []
    for index in range(0, 5):
        movie_details = get_search_results(moviename, index)
        all_movies.append(movie_details)
    return all_movies
