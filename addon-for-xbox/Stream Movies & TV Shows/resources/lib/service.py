import os, sys, time
# import requests
import packages.requests as requests
import urllib
import json
import utils.ListItemCreator as create
import utils.utils as utils
import xbmcgui.DialogProgress as DialogProgress

# in MB
BUFFER_SIZE_START = 50
BUFFER_SIZE_END = 10

path = "%s\\configuration.json" % os.getcwd()
json_data = open(path).read()
conf = utils.createObject(json_data)

API = conf.API
API_KEY = conf.API_KEY

HOST_ADDRESS = conf.HOST_ADDRESS
PORT = conf.PORT

def changeApi(new_api):
    global API
    API = new_api

def changeApiKey(new_api_key):
    global API_KEY
    API_KEY = new_api_key

def changeHostAddress(new_host_address):
    global HOST_ADDRESS
    HOST_ADDRESS = new_host_address

def changePort(new_port):
    global PORT
    PORT = new_port

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
    response = requests.get("http://%s:%s/search/%s/%s" % (HOST_ADDRESS, PORT, query, category))
    streams = utils.createObject(response.text)
    listitems = []
    for stream in streams:
        listitems.append(create.StreamListItem(stream))
    return streams, listitems

def getMagnet(torrent):
    payload = {
        "torrent": torrent.__dict__
    }
    response = requests.get("http://%s:%s/magnet" % (HOST_ADDRESS, PORT), headers={'Content-Type':'application/json', 'Accept': 'text/plain'}, json=payload)
    magnet = response.text
    return magnet

def startStreaming(magnet):
    payload = {
        "link": magnet
    }
    response = requests.post("http://%s:%s/torrents" % (HOST_ADDRESS, PORT), headers={'Content-Type':'application/json', 'Accept': 'text/plain'}, json=payload)
    infoHash = response.json().get('infoHash')
    return infoHash

def getInfoAboutStream(infoHash):
    while True:
        response = requests.get("http://%s:%s/torrents/%s" % (HOST_ADDRESS, PORT, infoHash))
        if response.status_code == 200:
            info = utils.createObject(response.text)
            return info
        else:
            DialogProgress.update(30, "Torrent is not ready. Retrying in 2 seconds...")
            if DialogProgress.iscanceled():
                return None
            time.sleep(2)

#TODO
"""
    >> Reimplement buffering algorithm.
    Current algorithm:
        1. Start downloading of whole file
        2. Buffer hard-coded  beggining of file and hope it's enough
        3. Checks if 'MOOV ATOM' is presented
            3.1 If not found, buffer hard-coded end of file and hope it containes 'MOOV ATOM'
        4. Start streaming

    New algorithm:
        1. Start downloading 'BUFFER_START_SIZE' beggining of file
        2. Start downloading 'BUFFER_END_SIZE' end of file
        3. Wait to buffer
        4. Check status of file 
            4.1 If error is presented (file corrupted or not found 'MOOV ATOM') repeat steps 1-3 (with multiplied BUFFER sizes with number of iteration) and check again
        5. Start downloading of whole file
        6. Start streaming
"""
def getStreamLink(infoHash, meta):
    info = getInfoAboutStream(infoHash)
    if meta['isMovie']:
        response = requests.post("http://%s:%s/torrents/%s/movie" % (HOST_ADDRESS, PORT, infoHash), headers={'User-Agent': 'xbox-streaming'})
        if response.status_code != 200:
            return None, "API returned {}: {}".format(response.status_code, response.text)
        filePath = response.text
        stream_link = "http://{}:{}/torrents/{}/files/{}".format(HOST_ADDRESS, PORT, infoHash, response.text)
    else:
        response = requests.post("http://{}:{}/torrents/{}/episode".format(HOST_ADDRESS, PORT, infoHash), headers={'Content-Type':'application/json', 'Accept': 'text/plain'}, json={'episode': meta['episode'], 'season': meta['season']})
        if response.status_code != 200:
            return None, "API returned {}: {}".format(response.status_code, response.text)
        filePath = response.text
        stream_link = "http://{}:{}/torrents/{}/files/{}".format(HOST_ADDRESS, PORT, infoHash, response.text)

    # check is this file created on File System (HDD)
    while True:
        response = requests.get("http://{}:{}/torrents/{}/file".format(HOST_ADDRESS, PORT, infoHash), headers={'User-Agent': 'xbox-streaming', 'Content-Type':'application/json'}, json={'filePath': filePath})
        if response.status_code == 404:
            DialogProgress.update(50, "File is not created. Retrying in 5 seconds...")
            if DialogProgress.iscanceled():
                return None, "User cancelled"
            time.sleep(5)

        else:
            DialogProgress.update(65, "Buffering...")
            break

    # wait to download first 50MB of file
    while True:
        info = getInfoAboutStream(infoHash)
        buffered = float(requests.get("http://{}:{}/torrents/{}/file".format(HOST_ADDRESS, PORT, infoHash), headers={'User-Agent': 'xbox-streaming', 'Content-Type':'application/json'}, json={'filePath': filePath}).text)

        if  buffered < BUFFER_SIZE_START:
            message = "Buffering: {:.2f} / {} Down: {:.2f} Up: {:.2f}".format(buffered, BUFFER_SIZE_START, utils.convertTo('KB', info.stats.speed.down), utils.convertTo('KB', info.stats.speed.up))
            DialogProgress.update(65, message)
            if DialogProgress.iscanceled():
                return None, "User cancelled"
            time.sleep(1)

        else:
            DialogProgress.update(70, "Checking status of 'MOOV ATOM'...")
            break

    # check status of moov atom and move it if needed
    while True:
        response = requests.get("{}?ffmpeg=probe".format(stream_link))

        if response.status_code == 500:
            DialogProgress.update(75, "I have to  move 'MOOV ATOM'. Proceeding...")
            # TODO Figure out how to move this shit
            response = requests.get("http://{}:{}/torrents/{}/moov-atom".format(HOST_ADDRESS, PORT, infoHash), headers={'User-Agent': 'xbox-streaming', 'Content-Type': 'application/json'}, json={'path': filePath, 'end': BUFFER_SIZE_END * 1024 * 1024})
            if response.status_code != 200:
                return None, "Error on API side"
            if DialogProgress.iscanceled():
                return None, "User cancelled"
            time.sleep(5)

        else:
            DialogProgress.update(95, "Succesfully downloaded MOOV ATOM")
            break

    return "{}?ffmpeg=remux".format(stream_link), "Everything is ready."