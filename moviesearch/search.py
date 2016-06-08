from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import re
import json


def get_soup(movie):
    movie = '+'.join(movie.split())
    url = "http://www.imdb.com/find?ref_=nv_sr_fn&q="+movie+"&s=all"
    br = Browser()
    br.open(url)
    try:
        link = list(br.links(url_regex=re.compile(r"/title/tt*")))[0]
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
        actors = []
        for actor in actor_list:
            str_act = str(actor).rpartition('itemprop="name"')[-1]
            actors.append(re.search('\>(.*?)\<', str_act).group(1))
        return actors
    except:
        return "N/A"


def get_director(movie, soup):
    try:
        director_list = soup.findAll('span', itemprop='director')
        directors = []
        for director in director_list:
            str_dir = str(director).rpartition('itemprop="name"')[-1]
            directors.append(re.search('\>(.*?)\<', str_dir).group(1))
        return directors
    except:
        return "N/A"


def get_writer(movie, soup):
    try:
        writer_list = soup.findAll('span', itemprop='creator')
        writers = []
        for writer in writer_list:
            str_writer = str(writer).rpartition('itemprop="name"')[-1]
            writers.append(re.search('\>(.*?)\<', str_writer).group(1))
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
        return rate
    except:
        return "N/A"


def get_genre(movie, soup):
    try:
        genre_list = soup.findAll('span', itemprop='genre')
        genres = []
        for genre in genre_list:
            str_gen = str(genre).rpartition('itemprop="genre"')[-1]
            genres.append(re.search('\>(.*?)\<', str_gen).group(1))
        return genres
    except:
        return "N/A"


def get_release_date(movie, soup):
    try:
        date = soup.find('meta', itemprop='datePublished').contents[0]
        return date
    except:
        return "N/A"


def get_all_details(movie):
    response = []

    soup = get_soup(movie)

    title = get_title(movie, soup)
    if title == "N/A":
        movie_response = "False"
        error_code = "Movie not found!"
        response.append({'Response': movie_response})
        response.append({'Error': error_code})
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

    response.append({'Title': title})
    response.append({'Year': year})
    response.append({'IMDb Rating': rating})
    response.append({'Votes': votes})
    response.append({'Runtime': duration})
    response.append({'Rated': content})
    response.append({'Genre': genre})
    response.append({'Director': director})
    response.append({'Writer': writer})
    response.append({'Actors': actors})
    return json.dumps(response)
