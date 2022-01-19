import os, sys
import requests
import urllib
import json
import ListItemCreator as create
import utils as utils

API = 'http://api.themoviedb.org/3'
API_KEY = 'b05365fc9e6222647f949031cbb9f759'

def getMoviesInTheatres(page):
    response = requests.get("%s/movie/now_playing?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.createBasicMovieListItem(movie))
    return movies

def getPopularMovies(page):
    response = requests.get("%s/movie/popular?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.createBasicMovieListItem(movie))
    return movies

def getUpcomingMovies(page):
    response = requests.get("%s/movie/upcoming?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.createBasicMovieListItem(movie))
    return movies

def getTopRatedMovies(page):
    response = requests.get("%s/movie/top_rated?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.createBasicMovieListItem(movie))
    return movies

def getOnTheAirTvShows(page):
    response = requests.get("%s/tv/on_the_air?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.createBasicTvShowItem(tv_show))
    return tv_shows

def getPopularTvShows(page):
    response = requests.get("%s/tv/popular?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.createBasicTvShowItem(tv_show))
    return tv_shows

def getAiringTodayTvShows(page):
    response = requests.get("%s/tv/airing_today?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.createBasicTvShowItem(tv_show))
    return tv_shows

def getTopRatedTvShows(page):
    response = requests.get("%s/tv/top_rated?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.createBasicTvShowItem(tv_show))
    return tv_shows

def searchMovies(input, page):
    response = requests.get("%s/search/movie?api_key=%s&language=en-US&query=%s&page=%s" % (API,API_KEY, input, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.createBasicMovieListItem(movie))
    return movies

def searchTvShows(input, page):
    response = requests.get("%s/search/tv?api_key=%s&language=en-US&query=%s&page=%s" % (API,API_KEY, input, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.createBasicTvShowItem(tv_show))
    return tv_shows

def getInfoAboutMovie(id):
    response = requests.get("%s/movie/%s?api_key=%s&language=en-US" % (API, id, API_KEY))
    movie = utils.createObject(response.text)
    return create.createFullMovieListItem(movie)

def getInfoAboutTvShow(id):
    response = requests.get("%s/tv/%s?api_key=%s&language=en-US" % (API, id, API_KEY))
    tv_show = utils.createObject(response.text)
    return create.createFullTvShowListItem(tv_show)

def getInfoAboutActor(id):
    response = requests.get("%s/person/%s?api_key=%s&language=en-US" % (API, id, API_KEY))
    actor = utils.createObject(response.text)
    return create.createFullActorListItem(actor)

def getActorsForMovie(id):
    response = requests.get("%s/movie/%s/credits?api_key=%s&language=en-US" % (API, id, API_KEY))
    dict = response.json()
    listitems = []
    for actor in dict.get('cast'):
        listitems.append(create.createBasicActorListItem(actor))
    return listitems[:20]

def getActorsForTvShow(id):
    response = requests.get("%s/tv/%s/credits?api_key=%s&language=en-US" % (API, id, API_KEY))
    dict = response.json()
    listitems = []
    for actor in dict.get('cast'):
        listitems.append(create.createBasicActorListItem(actor))
    return listitems[:20]

def getMoviesForActor(id):
    response = requests.get("%s/person/%s/movie_credits?api_key=%s&language=en-US" % (API, id, API_KEY))
    dict = response.json()
    listitems = []
    for movie in dict.get('cast'):
        listitems.append(create.createBasicMovieListItem(movie))
    return listitems[:20]

def getTvShowsForActor(id):
    response = requests.get("%s/person/%s/tv_credits?api_key=%s&language=en-US" % (API, id, API_KEY))
    dict = response.json()
    listitems = []
    for movie in dict.get('cast'):
        listitems.append(create.createBasicTvShowItem(movie))
    return listitems