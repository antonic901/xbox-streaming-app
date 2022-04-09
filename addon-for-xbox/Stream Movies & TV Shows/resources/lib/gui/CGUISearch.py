import os, sys
import xbmc, xbmcgui
import CGUIMovieInfo, CGUITvShowInfo

from resources.lib.utils import utils
from resources.lib import service
from resources.lib.xbmcgui import DialogProgress

class CGUISearch(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.query = kwargs['query']
        self.type = kwargs['type']
        self.items = kwargs['items']
        self.DETECTOR = 0
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        if self.DETECTOR is 0:
            assignIDs(self)
            self.getControl(self.cLabelSearch).setLabel("Search results for: %s" % self.query)
            self.getControl(self.cLabelType).setLabel("%s" % self.type)
            utils.populateContainer(self, self.cContainer, self.items)
            DialogProgress.update(99, 'Finishing...')
            self.setFocusId(self.cContainer)
            self.DETECTOR = 1
            xbmc.sleep(2000)
            DialogProgress.close()

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
	DialogProgress.create("XBMC4Xbox", "Calling TMDB API...")
	if "Movie" in item.getLabel():
		DialogProgress.update(25, 'Fetching info about Movie...')
		entity = service.getInfoAboutMovie(item.getProperty("id"))
		DialogProgress.update(50, 'Fetching actors...')
		actors = service.getActorsForMovie(item.getProperty("id"))
		DialogProgress.update(75, 'Opening Movie...')
		ui = CGUIMovieInfo.CGUIMovieInfo("MovieInfo.xml", utils.getScriptPath(), 'default', entity=entity, actors=actors)

	else:
		DialogProgress.update(25, 'Fetching info about TV Show...')
		entity = service.getInfoAboutTvShow(item.getProperty("id"))
		DialogProgress.update(50, 'Fetching actors...')
		actors = service.getActorsForTvShow(item.getProperty("id"))
		DialogProgress.update(75, 'Opening TV Show...')
		ui = CGUITvShowInfo.CGUITvShowInfo("TvShowInfo.xml", utils.getScriptPath(), 'default', entity=entity, actors=actors)
	
	ui.doModal()
	del ui