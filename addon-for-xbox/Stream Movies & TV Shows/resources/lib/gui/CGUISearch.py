import os, sys
import xbmc, xbmcgui
import CGUIMovieInfo, CGUITvShowInfo

from resources.lib.utils import utils
from resources.lib import service

class CGUISearch(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.query = kwargs['query']
        self.type = kwargs['type']
        self.items = kwargs['items']
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        assignIDs(self)
        self.getControl(self.cLabelSearch).setLabel("Search results for: %s" % self.query)
        self.getControl(self.cLabelType).setLabel("%s" % self.type)
        utils.populateContainer(self, self.cContainer, self.items)
        self.setFocusId(self.cContainer)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onFocus(self, controlId):
        pass

    def onClick(self, id):
        if id == self.cContainer:
            item = self.getControl(id).getSelectedItem()
            onClickControlPanelContainer(self, id)

def assignIDs(self):
    self.action_exitkeys_id = [10, 92]
    self.cLabelSearch = 34100
    self.cLabelType = 34002
    self.cContainer = 34200

def onClickControlPanelContainer(self, id):
	item = self.getControl(id).getSelectedItem()
	ui = None
	if "Movie" in item.getLabel():
		entity = service.getInfoAboutMovie(item.getProperty("id"))
		actors = service.getActorsForMovie(item.getProperty("id"))
		ui = CGUIMovieInfo.CGUIMovieInfo("MovieInfo.xml", self.__cwd__, 'default', __cwd__=self.__cwd__, entity=entity, actors=actors)
	else:
		entity = service.getInfoAboutTvShow(item.getProperty("id"))
		actors = service.getActorsForTvShow(item.getProperty("id"))
		ui = CGUITvShowInfo.CGUITvShowInfo("TvShowInfo.xml", self.__cwd__, 'default', __cwd__=self.__cwd__, entity=entity, actors=actors)
	ui.doModal()
	del ui