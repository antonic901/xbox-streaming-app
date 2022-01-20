import os, sys
import xbmc
import xbmcgui

class TestWindow(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 92]

        # xbmc.executebuiltin('Container.SetViewMode(50)')

        listitems = []
        listitem1 = xbmcgui.ListItem('My first item')
        listitems.append(listitem1)
        listitem2 = xbmcgui.ListItem('My first item')
        listitems.append(listitem2)

        self.clearList()

        for item in listitems:
            self.addItem(item)

        xbmc.sleep(100)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onFocus(self, controlId):
        pass