import os, sys
import xbmc
import xbmcgui

class CGUISearch(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        self.__cwd__ = kwargs['__cwd__']
        self.query = kwargs['query']
        self.type = kwargs['type']
        self.items = kwargs['items']
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 92]

        self.control_id_container = 34200

        self.getControl(34100).setLabel("Search results for: %s" % self.query)
        self.getControl(34002).setLabel("%s" % self.type)

        populateContainer(self, self.control_id_container, self.items)

        self.setFocusId(34200)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onFocus(self, controlId):
        pass

    def onClick(self, id):
        if(id == self.control_id_container):
            item = self.getControl(id).getSelectedItem()
            xbmcgui.Dialog().ok("Stream Movies and TV Shows", "This function is in development.")

def populateContainer(self, id, items):
	container = self.getControl(id)
	container.reset()
	for item in items:
		container.addItem(item)