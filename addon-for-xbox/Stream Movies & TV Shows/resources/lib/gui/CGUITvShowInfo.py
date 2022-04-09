# -*- coding: utf-8 -*-
import os, sys
import xbmc, xbmcgui
import CGUIActorInfo, CGUIStream

from resources.lib.utils import utils
from resources.lib import service
from resources.lib.xbmcgui import DialogProgress

class CGUITvShowInfo(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.entity = kwargs['entity']
        self.actors = kwargs['actors']
        self.DETECTOR = 0
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        if self.DETECTOR is 0:
            assignIDs(self)
            populateWithContent(self)
            DialogProgress.update(99, 'Finishing...')
            self.setFocusId(self.cButtonWatch)
            self.DETECTOR = 1
            xbmc.sleep(2000)
            DialogProgress.close()

    def onAction(self, action):
        if action == self.action_exitkeys_id[0]:
            self.getControl(6000).setVisible(False)
            self.getControl(6001).setVisible(True)
            self.getControl(6002).setVisible(True)

            self.setFocusId(4000)
        elif action == self.action_exitkeys_id[1]:
            self.close()

    def onClick(self, id):
        if id == self.cButtonWatch:
            self.getControl(6000).setVisible(True)
            self.getControl(6001).setVisible(False)
            self.getControl(6002).setVisible(False)

            self.setFocusId(34201)

        elif id == self.cContainerActors:
            onClickContainerActors(self, id)

        elif id == self.cContainerSeasons:
            item = self.getControl(id).getSelectedItem()
            episodes = service.getInfoAboutSeason(self.entity.getProperty('id'), item.getProperty('season_number'))
            utils.populateContainer(self, self.cContainerEpisodes, episodes)
            populateTextBox(self, self.cTextBoxOverview, episodes[0].getProperty('overview'))

        elif id == self.cContainerEpisodes:
            item = self.getControl(id).getSelectedItem()
            populateTextBox(self, self.cTextBoxOverview, item.getProperty('overview'))
        
        elif id == self.cButtonWatchEpisode:
            DialogProgress.create('XBMC4Xbox', 'Calling local API...')
            name = self.entity.getProperty('title')
            season = self.getControl(self.cContainerSeasons).getSelectedPosition() + 1
            episode = self.getControl(self.cContainerEpisodes).getSelectedPosition() + 1

            if season < 10:
                season = "0%s" % season

            if episode < 10:
                episode = "0%s" % episode
            
            DialogProgress.update(50, 'Finding available streams...')
            # streams, listitems = service.getStreams("%s s%se%s" % (self.entity.getProperty('title'), season, episode), "TV")
            streams, listitems = service.getStreams("%s s%s" % (self.entity.getProperty('title'), season), "TV")

            item = xbmcgui.ListItem("TV Show",
                iconImage=self.entity.getProperty('iconImage'),
                thumbnailImage=self.entity.getProperty('thumbImage')
            )

            item.setInfo('video', {
                'year': self.entity.getProperty('release_date').split("-")[0],
                'title': self.entity.getProperty('title'),
                # we are using this as container for TMDB_ID
                'tagline': self.entity.getProperty('id'),
                # we are using this as container for IMDB_ID
                'director': self.entity.getProperty('imdb_id'),
                # we are using this as container for episode number
                'plot': episode,
                # we are using this as container for season number
                'genre': season
            })

            meta = {
                'season': season,
                'episode': episode,
                'name': self.entity.getProperty('title'),
                'isMovie': False
            }

            ui = CGUIStream.CGUIStream('Stream.xml', utils.getScriptPath(), items=listitems, streams=streams, name=name, video_item=item, meta=meta)
            ui.doModal()
            del ui
    
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
    self.cTextBoxOverview = 2001
    self.cImageBackground = 3000
    self.cImagePoster = 3001
    self.cImageIMDB = 3002
    self.cImageAudio = 3003
    self.cButtonWatch = 4000
    self.cButtonWatchEpisode = 4001
    self.cContainerActors = 34200
    self.cContainerSeasons = 34201
    self.cContainerEpisodes = 34202

def populateWithContent(self):
    self.getControl(self.cLabelTitle).setLabel(self.entity.getProperty('title'))
    self.getControl(self.cLabelBasicInformation).setLabel(createTextForBasicInformation(self))
    self.getControl(self.cLabelDot).setLabel("•")
    self.getControl(self.cLabelRating).setLabel(self.entity.getProperty('vote_average'))
    self.getControl(self.cImageBackground).setImage(self.entity.getProperty('thumbImage'))
    self.getControl(self.cImagePoster).setImage(self.entity.getProperty('iconImage'))
    self.getControl(self.cTextBoxDescription).setText(self.entity.getProperty('overview'))

    utils.populateContainer(self, self.cContainerActors, self.actors)
    
    items = []
    for i in range(int(self.entity.getProperty('number_of_seasons'))):
        item = xbmcgui.ListItem('Season')
        item.setProperty('season_number', i + 1)
        items.append(item)
    utils.populateContainer(self, self.cContainerSeasons, items)

    episodes = service.getInfoAboutSeason(self.entity.getProperty('id'), 1)
    utils.populateContainer(self, self.cContainerEpisodes, episodes)

    populateTextBox(self, self.cTextBoxOverview, episodes[0].getProperty('overview'))

def populateTextBox(self, id, text):
    textBox = self.getControl(id)
    textBox.setText(text)

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