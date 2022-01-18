import os, sys
import xbmc
import xbmcgui

class CGUISearch(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.query = kwargs['query']
        self.type = kwargs['type']
        self.items = kwargs['items']
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 92]

        self.control_id_container = 34200
        self.control_container = self.getControl(self.control_id_container)

        self.getControl(34100).setLabel("Search results for: %s" % self.query)
        self.getControl(34002).setLabel("%s" % self.type)

        if "Movie" in self.type:
            createListItemsForMovies(self)
        elif "TV" in self.type:
            createListItemsForTvShows(self)

        self.setFocusId(34200)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onFocus(self, controlId):
        pass

    def onClick(self, id):
        if(id == 5000):
            self.close()

def createListItemsForMovies(self):
    self.control_container.reset()

    for movie in self.items:
        item = xbmcgui.ListItem(movie.title, movie.release_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
        item.setProperty('rating', movie.vote_average)
        self.control_container.addItem(item)

def createListItemsForTvShows(self):
    self.control_container.reset()

    for tv_show in self.items:
        item = xbmcgui.ListItem(tv_show.name, tv_show.first_air_date, iconImage=tv_show.poster_path, thumbnailImage=tv_show.poster_path)
        item.setProperty('rating', tv_show.vote_average)
        self.control_container.addItem(item)