# -*- coding: utf-8 -*-
import os, sys
import xbmc, xbmcgui
import CGUIActorInfo, CGUIStream

from resources.lib.utils import utils
from resources.lib import service

class CGUIMovieInfo(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.entity = kwargs['entity']
        self.actors = kwargs['actors']
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        assignIDs(self)
        populateWithContent(self)
        utils.populateContainer(self, self.cContainerActors, self.actors)
        self.setFocusId(self.cButtonWatch)
        xbmc.sleep(2000)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onClick(self, id):
        if id == self.cButtonWatch:
            name = self.entity.getProperty('title')
            streams, listitems = service.getStreams(name, "Movies")
            ui = CGUIStream.CGUIStream('Stream.xml', self.__cwd__, __cwd__=self.__cwd__, items=listitems, streams=streams, name=name)
            ui.doModal()
            del ui
        elif id == self.cContainerActors:
            onClickContainerActors(self, id)

    def onFocus(self, controlId):
        pass

def assignIDs(self):
    self.action_exitkeys_id = [10, 92]
    self.cLabelTitle = 1000
    self.cLabelBasicInformation = 1001
    self.cLabelDot = 1002
    self.cLabelRating = 1003
    self.cLabelAudioLanguage = 1004
    self.cTextBoxDescription = 2000
    self.cImageBackground = 3000
    self.cImagePoster = 3001
    self.cImageIMDB = 3002
    self.cImageAudio = 3003
    self.cButtonWatch = 4000
    self.cContainerActors = 34200

def populateWithContent(self):
    self.getControl(self.cLabelTitle).setLabel(self.entity.getProperty('title'))
    self.getControl(self.cLabelBasicInformation).setLabel(createTextForBasicInformation(self))
    self.getControl(self.cLabelDot).setLabel("•")
    self.getControl(self.cLabelRating).setLabel(self.entity.getProperty('vote_average'))
    self.getControl(self.cImageBackground).setImage(self.entity.getProperty('thumbImage'))
    self.getControl(self.cImagePoster).setImage(self.entity.getProperty('iconImage'))
    self.getControl(self.cTextBoxDescription).setText(self.entity.getProperty('overview'))

def onClickContainerActors(self, id):
    item = self.getControl(id).getSelectedItem()
    actor = service.getInfoAboutActor(item.getProperty('id'))
    movies = service.getMoviesForActor(item.getProperty('id'))
    tv_shows = service.getTvShowsForActor(item.getProperty('id'))
    ui = CGUIActorInfo.CGUIActorInfo("ActorInfo.xml", self.__cwd__, 'default', __cwd__=self.__cwd__, actor=actor, movies=movies, tv_shows=tv_shows)
    ui.doModal()
    del ui

def createTextForBasicInformation(self):
    return "%s  •  %s min  •  %s  •  %s" % (self.entity.getProperty('release_date'),self.entity.getProperty('runtime'),self.entity.getProperty('genres'), self.entity.getProperty('status'))