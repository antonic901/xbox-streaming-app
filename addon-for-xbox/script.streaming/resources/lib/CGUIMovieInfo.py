import os, sys
import xbmc
import xbmcgui

class CGUIMovieInfo(xbmcgui.WindowXML):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXML.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 92]
        # xbmc.executebuiltin('Container.SetViewMode(34000)')
        createLeftMenu(self)

        self.setFocusId(5000)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            self.close()

    def onFocus(self, controlId):
        pass

def createLeftMenu(self):
    self.control_id_menu1 = 34200
    # self.control_id_menu2 = 34201
    self.control_menu1 = self.getControl(self.control_id_menu1)
    # self.control_menu2 = self.getControl(self.control_id_menu2)
    listitems = [
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='https://www.themoviedb.org/t/p/h632/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='https://www.themoviedb.org/t/p/h632/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg'),
        xbmcgui.ListItem('Zendaya', iconImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg', thumbnailImage='http://www.themoviedb.org/t/p/w185/so3GqzuvXbYkNzQYNliAMB5rZzT.jpg')
    ]
    self.control_menu1.reset()
    # self.control_menu2.reset()
    for item in listitems:
        self.control_menu1.addItem(item)
        # self.control_menu2.addItem(item)
