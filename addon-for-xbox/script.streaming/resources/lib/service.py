import os, sys
import requests
import urllib
import json

API = 'http://api.themoviedb.org/3'
API_KEY = 'b05365fc9e6222647f949031cbb9f759'
IMAGE_BACKDROP = 'http://image.tmdb.org/t/p/w780'
IMAGE_POSTER = 'http://image.tmdb.org/t/p/w185'


def getMovieByIMDBId(id):
    response = requests.get("https://yts.mx/api/v2/list_movies.json?query_term=%s" % id)
    data = response.json()

def getMoviesInTheatres(page):
    response = requests.get("%s/movie/now_playing?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(Movie(movie))
    return movies

def getPopularMovies(page):
    response = requests.get("%s/movie/popular?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(Movie(movie))
    return movies

def getUpcomingMovies(page):
    response = requests.get("%s/movie/upcoming?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(Movie(movie))
    return movies

def getTopRatedMovies(page):
    response = requests.get("%s/movie/top_rated?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(Movie(movie))
    return movies

def getOnTheAirTvShows(page):
    response = requests.get("%s/tv/on_the_air?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(TvShow(tv_show))
    return tv_shows

def getPopularTvShows(page):
    response = requests.get("%s/tv/popular?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(TvShow(tv_show))
    return tv_shows

def getAiringTodayTvShows(page):
    response = requests.get("%s/tv/airing_today?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(TvShow(tv_show))
    return tv_shows

def getTopRatedTvShows(page):
    response = requests.get("%s/tv/top_rated?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(TvShow(tv_show))
    return tv_shows

class Movie:
    def __init__(self, dict):
        self.adult = dict.get('adult')
        self.backdrop_path = "%s%s" % (IMAGE_BACKDROP, dict.get('backdrop_path'))
        self.genre_ids = dict.get('genre_ids')
        self.id = dict.get('id')
        self.original_language = dict.get('original_language')
        self.original_title = dict.get('original_title')
        self.overview = dict.get('overview')
        self.popularity = dict.get('popularity')
        self.poster_path = "%s%s" % (IMAGE_POSTER, dict.get('poster_path'))
        self.release_date = dict.get('release_date').split('-')[0]
        self.title = dict.get('title')
        self.video = dict.get('video')
        self.vote_average = dict.get('vote_average')
        self.vote_count = dict.get('vote_count')

class TvShow:
    def __init__(self, dict):
        self.backdrop_path = "%s%s" % (IMAGE_BACKDROP, dict.get('backdrop_path'))
        self.first_air_date = dict.get('first_air_date')
        self.genre_ids = dict.get('genre_ids')
        self.id = dict.get('id')
        self.name = dict.get('name')
        self.origin_country = dict.get('origin_country')
        self.original_language = dict.get('original_language')
        self.original_name = dict.get('original_name')
        self.overview = dict.get('overview')
        self.popularity = dict.get('popularity')
        self.poster_path = "%s%s" % (IMAGE_POSTER, dict.get('poster_path'))
        self.vote_average = dict.get('vote_average')
        self.vote_count = dict.get('vote_count')