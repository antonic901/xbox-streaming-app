# -*- coding: utf-8 -*-
import os, sys
import xbmc
import xbmcgui
import service
import CGUIActorInfo

class CGUITvShowInfo(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.entity = kwargs['entity']
        self.actors = kwargs['actors']
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 92]
        assignIDs(self)
        populateWithContent(self)
        self.setFocusId(4000)
        xbmc.sleep(2000)

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
            populateContainer(self, self.cContainerEpisodes, episodes)
            populateTextBox(self, self.cTextBoxOverview, episodes[0].getProperty('overview'))

        elif id == self.cContainerEpisodes:
            item = self.getControl(id).getSelectedItem()
            populateTextBox(self, self.cTextBoxOverview, item.getProperty('overview'))
        
        elif id == self.cButtonWatchEpisode:
            xbmcgui.Dialog().ok("Stream Movies and TV Shows", "This function is in development.")
    
    def onFocus(self, controlId):
        pass

#1000 - labels
#2000 - textboxs
#3000 - images
#4000 - buttons
def assignIDs(self):
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

    populateContainer(self, self.cContainerActors, self.actors)
    
    items = []
    for i in range(int(self.entity.getProperty('number_of_seasons'))):
        item = xbmcgui.ListItem('Season')
        item.setProperty('season_number', i + 1)
        items.append(item)
    populateContainer(self, self.cContainerSeasons, items)

    episodes = service.getInfoAboutSeason(self.entity.getProperty('id'), 1)
    populateContainer(self, self.cContainerEpisodes, episodes)

    populateTextBox(self, self.cTextBoxOverview, episodes[0].getProperty('overview'))

def populateTextBox(self, id, text):
    textBox = self.getControl(id)
    textBox.setText(text)

def populateContainer(self, id, items):
    container = self.getControl(id)
    container.reset()
    for item in items:
        container.addItem(item)

def onClickContainerActors(self, id):
            item = self.getControl(id).getSelectedItem()
            actor = service.getInfoAboutActor(item.getProperty('id'))
            movies = service.getMoviesForActor(item.getProperty('id'))
            tv_shows = service.getTvShowsForActor(item.getProperty('id'))
            ui = CGUIActorInfo.CGUIActorInfo("actorInfo.xml", self.__cwd__, 'default', __cwd__=self.__cwd__, actor=actor, movies=movies, tv_shows=tv_shows)
            ui.doModal()
            del ui

def createTextForBasicInformation(self):
    return "%s  •  %s min  •  %s  •  %s" % (self.entity.getProperty('release_date'),self.entity.getProperty('runtime'),self.entity.getProperty('genres'), self.entity.getProperty('status'))