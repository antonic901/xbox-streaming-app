import os, sys
import packages.requests as requests
import urllib
import json
import utils.ListItemCreator as create
import utils.utils as utils

API = 'http://api.themoviedb.org/3'
API_KEY = 'f0d9239acde293e5222746bf11d1a3dc'

IP_ADDRESS = '192.168.0.10'
PORT = '9005'

def getMoviesInTheatres(page):
    response = requests.get("%s/movie/now_playing?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.BasicMovieListItem(movie))
    return movies

def getPopularMovies(page):
    response = requests.get("%s/movie/popular?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.BasicMovieListItem(movie))
    return movies

def getUpcomingMovies(page):
    response = requests.get("%s/movie/upcoming?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.BasicMovieListItem(movie))
    return movies

def getTopRatedMovies(page):
    response = requests.get("%s/movie/top_rated?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.BasicMovieListItem(movie))
    return movies

def getOnTheAirTvShows(page):
    response = requests.get("%s/tv/on_the_air?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.BasicTvShowItem(tv_show))
    return tv_shows

def getPopularTvShows(page):
    response = requests.get("%s/tv/popular?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.BasicTvShowItem(tv_show))
    return tv_shows

def getAiringTodayTvShows(page):
    response = requests.get("%s/tv/airing_today?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.BasicTvShowItem(tv_show))
    return tv_shows

def getTopRatedTvShows(page):
    response = requests.get("%s/tv/top_rated?api_key=%s&language=en-US&page=%s" % (API, API_KEY, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.BasicTvShowItem(tv_show))
    return tv_shows

def searchMovies(input, page):
    response = requests.get("%s/search/movie?api_key=%s&language=en-US&query=%s&page=%s" % (API,API_KEY, input, page))
    data = response.json()
    movies = []
    for movie in data['results']:
        movies.append(create.BasicMovieListItem(movie))
    return movies

def searchTvShows(input, page):
    response = requests.get("%s/search/tv?api_key=%s&language=en-US&query=%s&page=%s" % (API,API_KEY, input, page))
    data = response.json()
    tv_shows = []
    for tv_show in data['results']:
        tv_shows.append(create.BasicTvShowItem(tv_show))
    return tv_shows

def getInfoAboutMovie(id):
    response = requests.get("%s/movie/%s?api_key=%s&language=en-US" % (API, id, API_KEY))
    movie = utils.createObject(response.text)
    return create.FullMovieListItem(movie)

def getInfoAboutTvShow(id):
    response = requests.get("%s/tv/%s?api_key=%s&language=en-US" % (API, id, API_KEY))
    tv_show = utils.createObject(response.text)
    return create.FullTvShowListItem(tv_show)

def getInfoAboutActor(id):
    response = requests.get("%s/person/%s?api_key=%s&language=en-US" % (API, id, API_KEY))
    actor = utils.createObject(response.text)
    return create.FullActorListItem(actor)

def getActorsForMovie(id):
    response = requests.get("%s/movie/%s/credits?api_key=%s&language=en-US" % (API, id, API_KEY))
    dict = response.json()
    listitems = []
    for actor in dict.get('cast'):
        listitems.append(create.BasicActorListItem(actor))
    return listitems[:20]

def getActorsForTvShow(id):
    response = requests.get("%s/tv/%s/credits?api_key=%s&language=en-US" % (API, id, API_KEY))
    dict = response.json()
    listitems = []
    for actor in dict.get('cast'):
        listitems.append(create.BasicActorListItem(actor))
    return listitems[:20]

def getMoviesForActor(id):
    response = requests.get("%s/person/%s/movie_credits?api_key=%s&language=en-US" % (API, id, API_KEY))
    dict = response.json()
    listitems = []
    for movie in dict.get('cast'):
        listitems.append(create.BasicMovieListItem(movie))
    return listitems[:20]

def getTvShowsForActor(id):
    response = requests.get("%s/person/%s/tv_credits?api_key=%s&language=en-US" % (API, id, API_KEY))
    dict = response.json()
    listitems = []
    for movie in dict.get('cast'):
        listitems.append(create.BasicTvShowItem(movie))
    return listitems

def getInfoAboutSeason(id, number):
    response = requests.get("%s/tv/%s/season/%s?api_key=%s&language=en-US" % (API, id, number, API_KEY))
    season = utils.createObject(response.text)
    listitems = []
    for episode in season.episodes:
        listitems.append(create.EpisodeListItem(episode))
    return listitems

def getStreams(query, category):
    response = requests.get("http://%s:%s/search/%s/%s" % (IP_ADDRESS, PORT, query, category))
    streams = utils.createObject(response.text)
    listitems = []
    for stream in streams:
        listitems.append(create.StreamListItem(stream))
    return streams, listitems

def getMagnet(torrent):
    payload = {
        "torrent": torrent.__dict__
    }
    response = requests.get("http://%s:%s/magnet" % (IP_ADDRESS, PORT), headers={'Content-Type':'application/json', 'Accept': 'text/plain'}, json=payload)
    magnet = response.text
    return magnet

def startStreaming(magnet):
    payload = {
        "link": magnet
    }
    response = requests.post("http://%s:%s/torrents" % (IP_ADDRESS, PORT), headers={'Content-Type':'application/json', 'Accept': 'text/plain'}, json=payload)
    infoHash = response.json().get('infoHash')
    return infoHash

def getInfoAboutStream(infoHash):
    response = requests.get("http://%s:%s/torrents/%s" % (IP_ADDRESS, PORT, infoHash))
    info = utils.createObject(response.text)
    return info

def getStreamLink(infoHash):
    info = getInfoAboutStream(infoHash)
    for file in info.files:
        for extension in [".mp4", ".mkv", ".avi"]:
            if extension in file.name:
                return "http://%s:%s%s?ffmpeg=remux" % (IP_ADDRESS, PORT, file.link)
    return None