import os, sys
import xbmc, xbmcgui

IMAGE_BACKDROP = 'http://image.tmdb.org/t/p/w780'
IMAGE_POSTER = 'http://image.tmdb.org/t/p/w185'

def BasicMovieListItem(dict):
    item = xbmcgui.ListItem('Movie', 
        iconImage="%s%s" % (IMAGE_POSTER, dict.get('poster_path')),
        thumbnailImage="%s%s" % (IMAGE_BACKDROP, dict.get('backdrop_path')))

    item.setInfo('video', {
        'title': dict.get('title'),
        'rating': dict.get('vote_average'),
        'premiered': dict.get('release_date') 
	})

    item.setProperty("id", dict.get('id'))

    return item

def FullMovieListItem(entity):
    item = xbmcgui.ListItem('Movie', 
        iconImage="%s%s" % (IMAGE_POSTER, entity.poster_path),
        thumbnailImage="%s%s" % (IMAGE_BACKDROP, entity.backdrop_path))

    item.setInfo('video', {
        # 'genre': extractGenres(entity.genres),
        # 'country': extractCountries(entity.production_countries),
        'year': entity.release_date.split("-")[0],
        'rating': entity.vote_average,
        'title': entity.title,
        'originaltitle': entity.original_title,
        # conflict with episode item (85: CGUITvShowInfo.py)
        # 'plot': entity.overview,
        'duration': entity.runtime,
        'premiered': entity.release_date,
        'votes': entity.vote_count,
        # we are using this as container for TMDB_ID
        'tagline': entity.id,
        # we are using this as container for IMDB_ID
        'director': entity.imdb_id
    })

    item.setProperty("adult", entity.adult)
    item.setProperty("iconImage", "%s%s" % (IMAGE_POSTER,entity.poster_path))
    item.setProperty('thumbImage', "%s%s" % (IMAGE_BACKDROP, entity.backdrop_path))
    item.setProperty("belongs_to_collection", entity.belongs_to_collection)
    item.setProperty("budget", entity.budget)
    item.setProperty("genres", extractNamesFromList(entity.genres))
    item.setProperty("homepage", entity.homepage)
    item.setProperty("id", entity.id)
    item.setProperty("imdb_id", entity.imdb_id)
    item.setProperty("original_language", entity.original_language)
    item.setProperty("original_title", entity.original_title)
    item.setProperty("overview", entity.overview)
    item.setProperty("popularity", entity.popularity)
    item.setProperty("production_companies", entity.production_companies)
    item.setProperty("production_countries", entity.production_countries)
    item.setProperty("release_date", entity.release_date)
    item.setProperty("revenue", entity.revenue)
    item.setProperty("runtime", entity.runtime)
    item.setProperty("spoken_languages", entity.spoken_languages)
    item.setProperty("status", entity.status)
    item.setProperty("tagline", entity.tagline)
    item.setProperty("title", entity.title)
    item.setProperty("vote_average", entity.vote_average)
    item.setProperty("vote_count", entity.vote_count)

    return item

#represents basic information about some tv show
def BasicTvShowItem(dict):
    item = xbmcgui.ListItem('TV Show', 
        iconImage="%s%s" % (IMAGE_POSTER, dict.get('poster_path')),
        thumbnailImage="%s%s" % (IMAGE_BACKDROP, dict.get('backdrop_path')))

    item.setInfo('video', {
        'title': dict.get('name'),
        'rating': dict.get('vote_average'),
        'premiered': dict.get('first_air_date')
	})

    item.setProperty("id", dict.get('id'))

    return item

def FullTvShowListItem(entity):
    item = xbmcgui.ListItem('TV Show',
        iconImage="%s%s" % (IMAGE_POSTER, entity.poster_path),
        thumbnailImage="%s%s" % (IMAGE_BACKDROP, entity.backdrop_path))

    item.setInfo('video', {
        # 'genre': extractGenres(entity.genres),
        # 'country': extractCountries(entity.production_countries),
        'year': entity.first_air_date.split("-")[0],
        'rating': entity.vote_average,
        'title': entity.name,
        # 'originaltitle': entity.original_title,
        'plot': entity.overview,
        'duration': entity.episode_run_time[0],
        'premiered': entity.first_air_date,
        'votes': entity.vote_count,
        # we are using this as container for TMDB_ID
        'tagline': entity.id
        # we are using this as container for IMDB_ID
        # 'director': entity.imdb_id
    })
    
    item.setProperty("iconImage", "%s%s" % (IMAGE_POSTER,entity.poster_path))
    item.setProperty('thumbImage', "%s%s" % (IMAGE_POSTER, entity.backdrop_path))
    item.setProperty('runtime', entity.episode_run_time[0])
    item.setProperty('release_date', entity.first_air_date)
    item.setProperty('genres', extractNamesFromList(entity.genres))
    item.setProperty('id', entity.id)
    item.setProperty('status', getStatus(entity.in_production))
    item.setProperty('title', entity.name)
    item.setProperty('number_of_episodes', entity.number_of_episodes)
    item.setProperty('number_of_seasons', entity.number_of_seasons)
    item.setProperty('overview', entity.overview)
    item.setProperty('seasons', entity.seasons)
    item.setProperty('vote_average', entity.vote_average)

    return item

def BasicActorListItem(dict):
    item = xbmcgui.ListItem('Actor',
        iconImage="%s%s" % (IMAGE_POSTER, dict.get('profile_path')))

    item.setProperty('id', dict.get('id'))
    item.setProperty('name', dict.get('name'))
    item.setProperty('character', dict.get('character'))
    
    return item

def FullActorListItem(entity):
    item = xbmcgui.ListItem('Actor',
        iconImage="%s%s" % (IMAGE_POSTER, entity.profile_path))

    item.setProperty('also_known_as', entity.also_known_as)
    item.setProperty('biography', entity.biography)
    item.setProperty('birthday', entity.birthday)
    item.setProperty('gender', getGender(entity.gender))
    item.setProperty('id', entity.id)
    item.setProperty('imdb_id', entity.imdb_id)
    item.setProperty('known_for_department', entity.known_for_department)
    item.setProperty('name', entity.name)
    item.setProperty('place_of_birth', entity.place_of_birth)
    item.setProperty('profile_path', "%s%s" % (IMAGE_BACKDROP, entity.profile_path))
    
    return item

def EpisodeListItem(entity):
    item = xbmcgui.ListItem(entity.name)

    item.setProperty('name', entity.name)
    item.setProperty('overview', entity.overview)
    item.setProperty('episode_number', entity.episode_number)
    item.setProperty('season_number', entity.season_number)

    return item

def StreamListItem(entity):
    item = xbmcgui.ListItem('Stream')

    item.setProperty('title', entity.title)
    item.setProperty('seeds', entity.seeds)
    item.setProperty('peers', entity.peers)
    item.setProperty('size', entity.size)
    item.setProperty('provider', entity.provider)

    return item

def extractNamesFromList(list):
    string = ''
    i = 0
    for item in list:
        if i == len(list) - 1:
            string = string + item.name
        else:
            string = string + item.name + "/"
        i = i + 1
    return string

def extractGenres(list):
    genres = []
    for item in list:
        genres.append(item.name)
    return genres

def extractCountries(list):
    countries = []
    for item in list:
        countries.append(item.name)
    return countries

def getGender(id):
    dict = {
        0: 'Unknown',
        1: 'Female',
        2: 'Male',
        3: 'Unknown'
    }
    return dict[id]

def getStatus(status):
    if status:
        return 'Returning Series'
    else:
        return 'Ended'