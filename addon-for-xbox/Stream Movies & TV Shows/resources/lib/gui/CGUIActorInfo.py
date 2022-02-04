# -*- coding: utf-8 -*-
import os, sys
import xbmc, xbmcgui
import CGUIMovieInfo, CGUITvShowInfo

from resources.lib.utils import utils
from resources.lib import service

class CGUIActorInfo(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.entity = kwargs['actor']
        self.movies = kwargs['movies']
        self.tv_shows = kwargs['tv_shows']
        self.DETECTOR = 0
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        if self.DETECTOR is 0:
            assignIDs(self)
            populateWithContent(self)
            utils.populateContainer(self, self.cPanelMovies, self.movies)
            utils.populateContainer(self, self.cPanelTvShows, self.tv_shows)
            self.setFocusId(5000)
            self.DETECTOR = 1
            xbmc.sleep(2000)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onFocus(self, controlId):
        pass

    def onClick(self, id):
        if(id == 5000):
            self.close()
        elif(id == 5001):
            xbmcgui.Dialog().ok('Biography', self.entity.getProperty('biography'))
        elif id in [self.cPanelMovies, self.cPanelTvShows]:
            onClickControlPanelContainer(self, id)

def assignIDs(self):
    self.action_exitkeys_id = [10, 92]
    self.cLabelActorName = 1000
    self.cLabelBasicInformation = 1001
    self.cLabelAge = 1002
    self.cLabelBorn = 1003
    self.cLabelPlaceOfBirth = 1004
    self.cTextBoxBiography = 2000
    self.cImageActor = 3000
    self.cPanelMovies = 34200
    self.cPanelTvShows = 34201

def populateWithContent(self):
    self.getControl(self.cLabelActorName).setLabel(self.entity.getProperty('name'))
    self.getControl(self.cLabelBasicInformation).setLabel(createTextForBasicInformation(self))
    self.getControl(self.cLabelBorn).setLabel(self.entity.getProperty('birthday'))
    self.getControl(self.cLabelPlaceOfBirth).setLabel(self.entity.getProperty('place_of_birth'))
    self.getControl(self.cTextBoxBiography).setText(self.entity.getProperty('biography'))
    self.getControl(self.cImageActor).setImage(self.entity.getProperty('profile_path'))

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

def createTextForBasicInformation(self):
    return "%s  •  Known for: %s  •  %s  •  %s" % (self.entity.getProperty('gender'), self.entity.getProperty('known_for_department'), self.entity.getProperty('place_of_birth'), self.entity.getProperty('birthday'))