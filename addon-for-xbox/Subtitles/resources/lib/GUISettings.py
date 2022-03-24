import os, sys
import xbmc, xbmcgui

import DialogProgress
import opensubtitles
import utils

class GUISettings(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        assignIDs(self)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            # DialogProgress.delete()
            self.close()

    def onFocus(self, id):
        pass

    def onClick(self, id):
        pass

def assignIDs(self):
    pass