import os, sys, urllib
import xbmc, xbmcgui
import CGUIMovieInfo, CGUITvShowInfo

from resources.lib.utils import utils
from resources.lib import service
from resources.lib.xbmcgui import DialogProgress

class CGUIStream(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.streams = kwargs['streams']
        self.items = kwargs['items']
        self.name = kwargs['name']
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        assingIDs(self)
        self.getControl(self.cLabelTitle).setLabel("Available streams for %s" % self.name)
        utils.populateContainer(self, self.cListStream, self.items)
        DialogProgress.update(99, 'Finishing...')
        self.setFocusId(self.cListStream)
        xbmc.sleep(2000)
        DialogProgress.close()

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onFocus(self, controlId):
        pass

    def onClick(self, id):
        if id == self.cListStream:
            DialogProgress.create('XBMC4Xbox', 'Starting stream...')
            DialogProgress.update(0, 'Getting torrent...')
            index = self.getControl(id).getSelectedPosition()
            torrent = self.streams[index]

            DialogProgress.update(15, 'Getting magnet link of torrent...')
            magnet = service.getMagnet(torrent)
            
            DialogProgress.update(30, 'Starting stream...')
            infoHash = service.startStreaming(magnet)

            xbmc.sleep(2500)
            DialogProgress.update(45, 'Buffering...')

            xbmc.sleep(2500)
            DialogProgress.update(60, 'Buffering...')

            xbmc.sleep(2500)
            DialogProgress.update(75, 'Getting local stream link...')
            link = service.getStreamLink(infoHash)
            DialogProgress.update(90, 'Starting player...')
            title = urllib.unquote_plus(self.name)
            item = xbmcgui.ListItem(title)
            xbmc.Player().play(link, item)
            
            DialogProgress.close()

            self.close()

def assingIDs(self):
    self.action_exitkeys_id = [10, 92]
    self.cListStream = 34000
    self.cLabelTitle = 1000