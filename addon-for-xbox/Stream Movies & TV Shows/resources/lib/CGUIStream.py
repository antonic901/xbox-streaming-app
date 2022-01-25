import os, sys, urllib
import xbmc, xbmcgui
import service
import CGUIMovieInfo, CGUITvShowInfo

class CGUIStream(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.streams = kwargs['streams']
        self.items = kwargs['items']
        self.name = kwargs['name']
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def __del__(self):
        print("CGUIStream windows is destroyed.")

    def onInit(self):
        self.action_exitkeys_id = [10, 92]
        self.cListStream = 34000
        self.cLabelTitle = 1000

        self.getControl(self.cLabelTitle).setLabel("Available streams for %s" % self.name)
        populateContainer(self, self.cListStream, self.items)

        self.setFocusId(self.cListStream)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onFocus(self, controlId):
        pass

    def onClick(self, id):
        if id == self.cListStream:
            index = self.getControl(id).getSelectedPosition()
            torrent = self.streams[index]
            magnet = service.getMagnet(torrent)
            infoHash = service.startStreaming(magnet)

            pDialog = xbmcgui.DialogProgress()
            pDialog.create('Kodi', 'Starting stream...')
            pDialog.update(0, 'Starting stream...')

            xbmc.sleep(2500)
            pDialog.update(25, 'Buffering...')

            xbmc.sleep(2500)
            pDialog.update(50, 'Buffering...')

            xbmc.sleep(2500)
            pDialog.update(75, 'Starting player...')

            link = service.getStreamLink(infoHash)
            title = urllib.unquote_plus(self.name)
            # thumb = urllib.unquote_plus(thumb)
            item = xbmcgui.ListItem(title)
            xbmc.Player().play(link, item)
            
            pDialog.close()
            del pDialog

            self.close()

def populateContainer(self, id, items):
	container = self.getControl(id)
	container.reset()
	for item in items:
		container.addItem(item)