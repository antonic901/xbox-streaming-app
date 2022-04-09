import os, sys, urllib
import xbmc, xbmcgui
import CGUIMovieInfo, CGUITvShowInfo

from resources.lib.utils import utils
from resources.lib import service
from resources.lib.xbmcgui import DialogProgress

class CGUIStream(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        self.streams = kwargs['streams']
        self.items = kwargs['items']
        self.name = kwargs['name']
        self.video_item = kwargs['video_item']
        self.meta = kwargs['meta']
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

            DialogProgress.update(10, 'Getting magnet link of torrent...')
            magnet = service.getMagnet(torrent)
            
            DialogProgress.update(20, 'Starting download...')
            infoHash = service.startStreaming(magnet)

            DialogProgress.update(25, 'Getting local stream link...')
            # DialogProgress.close()
            link, message = service.getStreamLink(infoHash, self.meta)
            
            if link is None:
                DialogProgress.close()
                xbmc.executebuiltin('Notification(%s, Could not generate stream link,5000,DefaultIconInfo.png)' % message)
                self.close()

            DialogProgress.update(95, 'Starting player...')
            xbmc.Player().play(link, self.video_item)
            
            DialogProgress.close()

            self.close()

def assingIDs(self):
    self.action_exitkeys_id = [10, 92]
    self.cListStream = 34000
    self.cLabelTitle = 1000