import os, sys
import xbmc
import xbmcgui

IMAGE_BACKDROP = 'http://image.tmdb.org/t/p/w780'
IMAGE_POSTER = 'http://image.tmdb.org/t/p/w185'

#represents basic information about some movie
def createBasicMovieListItem(dict):
    item = xbmcgui.ListItem('Movie', 
                            iconImage="%s%s" % (IMAGE_POSTER, dict.get('poster_path')),
                            thumbnailImage="%s%s" % (IMAGE_BACKDROP, dict.get('backdrop_path')))

    item.setInfo('video', {
			'title': dict.get('title'),
            'rating': dict.get('vote_average'),
            'premiered': dict.get('release_date') 
	})

    return item

#represents basic information about some tv show
def createBasicTvShowItem(dict):
    item = xbmcgui.ListItem('TV Show', 
                            iconImage="%s%s" % (IMAGE_POSTER, dict.get('poster_path')),
                            thumbnailImage="%s%s" % (IMAGE_BACKDROP, dict.get('backdrop_path')))

    item.setInfo('video', {
			'title': dict.get('name'),
            'rating': dict.get('vote_average'),
            'premiered': dict.get('first_air_date')
	})

    return item