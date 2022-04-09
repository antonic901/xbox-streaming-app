# -*- coding: utf-8 -*-
import os, sys
import xbmc, xbmcgui
import CGUIActorInfo, CGUIStream

from resources.lib.utils import utils
from resources.lib import service
from resources.lib.xbmcgui import DialogProgress

class CGUIMovieInfo(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.entity = kwargs['entity']
        self.actors = kwargs['actors']
        self.DETECTOR = 0
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        if self.DETECTOR is 0:
            assignIDs(self)
            populateWithContent(self)
            utils.populateContainer(self, self.cContainerActors, self.actors)
            DialogProgress.update(99, 'Finishing...')
            self.setFocusId(self.cButtonWatch)
            self.DETECTOR = 1
            xbmc.sleep(2000)
            DialogProgress.close()

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onClick(self, id):
        if id == self.cButtonWatch:
            DialogProgress.create('XBMC4Xbox', 'Calling local API...')
            query = self.entity.getProperty('title') + " " + self.entity.getProperty('release_date').split("-")[0]
            DialogProgress.update(50, 'Finding available streams...')
            streams, listitems = service.getStreams(query, "Movies")

            meta = {
                'season': None,
                'episode': None,
                'name': self.entity.getProperty('title'),
                'isMovie': True
            }

            ui = CGUIStream.CGUIStream('Stream.xml', utils.getScriptPath(), items=listitems, streams=streams, name=query, video_item=self.entity, meta=meta)
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
    DialogProgress.create("XMBC4Xbox", 'Calling TMDB API...')
    DialogProgress.update(25, 'Fetching info about actor...')
    actor = service.getInfoAboutActor(item.getProperty('id'))
    DialogProgress.update(50, 'Fetching Movies for actor...')
    movies = service.getMoviesForActor(item.getProperty('id'))
    DialogProgress.update(75, 'Fetching TV Shows for actor...')
    tv_shows = service.getTvShowsForActor(item.getProperty('id'))
    DialogProgress.update(80, 'Opening actor...')
    ui = CGUIActorInfo.CGUIActorInfo("ActorInfo.xml", utils.getScriptPath(), 'default', actor=actor, movies=movies, tv_shows=tv_shows)
    ui.doModal()
    del ui

def createTextForBasicInformation(self):
    return "%s  •  %s min  •  %s  •  %s" % (self.entity.getProperty('release_date'),self.entity.getProperty('runtime'),self.entity.getProperty('genres'), self.entity.getProperty('status'))