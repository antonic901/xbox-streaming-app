# -*- coding: utf-8 -*-
import os, sys
import xbmc
import xbmcgui
import service
import CGUIMovieInfo

class CGUIActorInfo(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.entity = kwargs['actor']
        self.movies = kwargs['movies']
        self.tv_shows = kwargs['tv_shows']
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 92]
        generateIDs(self)
        populateWithContent(self)
        populateContainer(self, self.cPanelMovies, self.movies)
        populateContainer(self, self.cPanelTvShows, self.tv_shows)
        self.setFocusId(5000)
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
        elif id == self.cPanelMovies:
            onClickControlPanelContainer(self, id)
        elif id == self.cPanelTvShows:
            xbmcgui.Dialog().ok('Stream Movies & TV Shows', "This funcionality is in development.")


#1000 - labels
#2000 - textboxs
#3000 - images
#4000 - buttons
def generateIDs(self):
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
    # self.getControl(self.cLabelAge).setLabel(self.entity.getProperty(23))
    self.getControl(self.cLabelBorn).setLabel(self.entity.getProperty('birthday'))
    self.getControl(self.cLabelPlaceOfBirth).setLabel(self.entity.getProperty('place_of_birth'))
    self.getControl(self.cTextBoxBiography).setText(self.entity.getProperty('biography'))
    self.getControl(self.cImageActor).setImage(self.entity.getProperty('profile_path'))

def onClickControlPanelContainer(self, id):
	item = self.getControl(id).getSelectedItem()
	entity = service.getInfoAboutMovie(item.getProperty("id"))
	actors = service.getActorsForMovie(item.getProperty("id"))
	ui = CGUIMovieInfo.CGUIMovieInfo("movieInfo.xml", self.__cwd__, 'default', __cwd__=self.__cwd__, entity=entity, actors=actors)
	ui.doModal()
	del ui

def populateContainer(self, id, items):
    container = self.getControl(id)
    container.reset()
    for item in items:
        container.addItem(item)

def createTextForBasicInformation(self):
    return "%s  •  Known for: %s  •  %s  •  %s" % (self.entity.getProperty('gender'), self.entity.getProperty('known_for_department'), self.entity.getProperty('place_of_birth'), self.entity.getProperty('birthday'))