import os, sys
import xbmc
import xbmcgui
import service

class GUI(xbmcgui.WindowXML):

	def __init__(self, *args, **kwargs):
		xbmcgui.WindowXML.__init__(self, *args, **kwargs)

	def onInit(self):
		self.action_exitkeys_id = [10, 92]
		xbmc.executebuiltin('Container.SetViewMode(34000)')
		createLeftMenu(self)
		# xbmc.sleep(100)
		self.setFocusId(34000)

		self.control_id_label1 = 34002

	def onAction(self, action):
		if action in self.action_exitkeys_id:
			self.close()

	def onFocus(self, controlId):
		pass

	def onClick(self, id):
		if id == self.control_id_menu:
			item = self.control_menu.getSelectedItem()
			if "Movies" == item.getLabel():
				service.getPopularMovies()
				self.getControl(self.control_id_label1).setLabel(item.getLabel())
			elif "TV Shows" == item.getLabel():
				service.getPopularTvShows()
				self.getControl(self.control_id_label1).setLabel(item.getLabel())
			elif "Search" in item.getLabel():
				keyboard = xbmc.Keyboard()
				keyboard.doModal()
				if(keyboard.isConfirmed() and keyboard.getText() != ""):
					enteredText = keyboard.getText()
					self.getControl(self.control_id_label1).setLabel('Results for %s' % enteredText)
				else:
					self.getControl(self.control_id_label1).setLabel('User cancelled search')
				del keyboard

def createLeftMenu(self):
		self.control_id_menu = 34000
		self.control_menu = self.getControl(self.control_id_menu)
		listitems = [
			xbmcgui.ListItem('Movies', iconImage='icons/32/movies.png'), 
			xbmcgui.ListItem('TV Shows', iconImage='icons/32/tvshows.png'),
			xbmcgui.ListItem('Search Movies...', iconImage='icons/32/music.png'),
			xbmcgui.ListItem('Search TV Shows...', iconImage='icons/32/searchtvshows.png')
		]
		self.control_menu.reset()
		for item in listitems:
			self.control_menu.addItem(item)
