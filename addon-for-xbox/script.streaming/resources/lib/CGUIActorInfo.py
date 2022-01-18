import os, sys
import xbmc
import xbmcgui

class CGUIActorInfo(xbmcgui.WindowXML):

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

    def onClick(self, id):
        if(id == 5000):
            self.close()
        elif(id == 5001):
            xbmcgui.Dialog().ok('Biography', 'Here goes biography of actor.')

def createLeftMenu(self):
    self.control_id_menu1 = 34200
    self.control_id_menu2 = 34201
    self.control_menu1 = self.getControl(self.control_id_menu1)
    self.control_menu2 = self.getControl(self.control_id_menu2)
    listitems = [
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg'),
        xbmcgui.ListItem('Spider-Man: No Way Home', iconImage='http://www.themoviedb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg')
    ]
    self.control_menu1.reset()
    self.control_menu2.reset()
    for item in listitems:
        self.control_menu1.addItem(item)
        self.control_menu2.addItem(item)
