import os, sys
import xbmc, xbmcgui
import CGUISearch, CGUIMovieInfo, CGUITvShowInfo

from resources.lib.utils import utils
from resources.lib import service
from resources.lib.xbmcgui import DialogProgress

class CGUIMain(xbmcgui.WindowXML):

	def __init__(self, *args, **kwargs):
		self.DETECTOR = 0
		xbmcgui.WindowXML.__init__(self, *args, **kwargs)

	def onInit(self):
		"""
			Let's say you opened new window from this window (i.e. you opened some Movie).
			When closing second Window constructor of this Window will be called again for some reason.
			This behavior reproduce some weird glitches and sometimes crashes or freezes Xbox.
			Workaround for this is to have variable 'Detector' which initial value is 0. When constructor is called
			for the firstime value of 'Detector' will be set to 1. So when you open another window and close it,
			code inside 'if' statement will not be executed (we only want this code to be executed one time).
		"""
		if self.DETECTOR is 0:
			DialogProgress.create('XBMC4Xbox', 'Initializing home page...')
			DialogProgress.update(25, 'Assigning IDs...')
			assignIDs(self)
			DialogProgress.update(50, 'Creating left menu...')
			createLeftMenu(self)
			DialogProgress.update(75, 'Getting movies for home screen...')
			getMoviesForHomeScreen(self)
			DialogProgress.update(99, 'Finishing...')
			self.setFocusId(self.control_id_menu)
			self.DETECTOR = 1
			xbmc.sleep(2000)
			DialogProgress.close()

	def onAction(self, action):
		if action in self.action_exitkeys_id:
			DialogProgress.delete()
			self.close()

		#274 is 'Start' button
		elif action.getButtonCode() == 274:
			# remember component which have focus
			focusId = self.getFocusId()
			
			import resources.lib.gui.CGUISettings as CGUISettings
			ui = CGUISettings.CGUISettings('_Settings.xml', utils.getScriptPath(), 'default', allow_cancel=True)
			ui.doModal()
			del ui

			# return focus to component
			self.setFocusId(focusId)

	def onFocus(self, controlId):
		pass

	def onClick(self, id):
		if id == self.control_id_menu:
			onClickControlPanelMenu(self)
		elif id in [self.control_id_panel_in_theatres, 
					self.control_id_panel_popular, 
					self.control_id_panel_upcoming, 
					self.control_id_panel_top_rated]:
			onClickControlPanelContainer(self, id)

def assignIDs(self):
	self.action_exitkeys_id = [10, 92]

	self.control_id_panel_in_theatres = 34200
	self.control_id_panel_popular = 34201
	self.control_id_panel_upcoming = 34202
	self.control_id_panel_top_rated = 34203

	self.control_id_menu = 34000

	self.control_id_label1 = 34002
	self.control_id_label2 = 34100
	self.control_id_label3 = 34101
	self.control_id_label4 = 34102
	self.control_id_label5 = 34103

def createLeftMenu(self):
		self.control_menu = self.getControl(self.control_id_menu)
		listitems = [
			xbmcgui.ListItem('Movies', iconImage='icons/32/movies.png'), 
			xbmcgui.ListItem('TV Shows', iconImage='icons/32/tvshows.png'),
			xbmcgui.ListItem('Search Movies...', iconImage='icons/32/searchtvshows.png'),
			xbmcgui.ListItem('Search TV Shows...', iconImage='icons/32/searchtvshows.png')
		]
		self.control_menu.reset()
		for item in listitems:
			self.control_menu.addItem(item)

#Called when user click item on left menu
def changeLabelsForPanels(self, label2, label3, label4, label5):
	self.getControl(self.control_id_label2).setLabel(label2)
	self.getControl(self.control_id_label3).setLabel(label3)
	self.getControl(self.control_id_label4).setLabel(label4)
	self.getControl(self.control_id_label5).setLabel(label5)

#called when 'Movies' button is pressed
def getMoviesForHomeScreen(self):
	utils.populateContainer(self, self.control_id_panel_in_theatres, service.getMoviesInTheatres(1))
	utils.populateContainer(self, self.control_id_panel_popular, service.getPopularMovies(1))
	utils.populateContainer(self, self.control_id_panel_upcoming, service.getUpcomingMovies(1))
	utils.populateContainer(self, self.control_id_panel_top_rated, service.getTopRatedMovies(1))

#called when 'TV Shows' button is pressed
def getTvShowsForHomeScreen(self):
	utils.populateContainer(self, self.control_id_panel_in_theatres, service.getOnTheAirTvShows(1))
	utils.populateContainer(self, self.control_id_panel_popular, service.getPopularTvShows(1))
	utils.populateContainer(self, self.control_id_panel_upcoming, service.getAiringTodayTvShows(1))
	utils.populateContainer(self, self.control_id_panel_top_rated, service.getTopRatedTvShows(1))

#Called when 'Search" button is pressed
def onClickControlPanelMenu(self):
	item = self.control_menu.getSelectedItem()
	position = self.control_menu.getSelectedPosition()
	if position == 0:
		DialogProgress.create("XBMC4Xbox", "Calling TMDB API...")
		DialogProgress.update(50, "Fetching Movies...")
		getMoviesForHomeScreen(self)
		DialogProgress.update(99, "Finishing...")
		self.getControl(self.control_id_label1).setLabel(item.getLabel())
		changeLabelsForPanels(self, 'In Theatres', 'Popular Movies', 'Upcoming Movies', 'Top Rated')
		DialogProgress.close()
	elif position == 1:
		DialogProgress.create("XBMC4Xbox", "Calling TMDB API...")
		DialogProgress.update(50, "Fetching TV Shows...")
		getTvShowsForHomeScreen(self)
		DialogProgress.update(99, "Finishing...")
		self.getControl(self.control_id_label1).setLabel(item.getLabel())
		changeLabelsForPanels(self, 'On The Air', 'Popular TV Shows', 'Airing Today', 'Top Rated')
		DialogProgress.close()
	elif position in [2,3]:
		keyboard = xbmc.Keyboard()
		keyboard.doModal()
		keyboardConfirmed = keyboard.isConfirmed()
		enteredText = keyboard.getText()
		del keyboard
		if(keyboardConfirmed and enteredText != ""):
			ui = None		
			items = []
			DialogProgress.create("XBMC4Xbox", "Calling TMDB API...")
			if position == 2:
				DialogProgress.update(50, "Searching Movies...")
				items = service.searchMovies(enteredText, 1)
				DialogProgress.update(75, "Opening search results...")
				ui = CGUISearch.CGUISearch('Search.xml', utils.getScriptPath(), 'default', query=enteredText, type='Movies', items=items)

			else:
				DialogProgress.update(50, "Searching TV Shows...")
				items = service.searchTvShows(enteredText, 1)
				DialogProgress.update(99, "Opening search results...")
				ui = CGUISearch.CGUISearch('Search.xml', utils.getScriptPath(), 'default', query=enteredText, type='TV Shows', items=items)

			ui.doModal()
			del ui

		else:
			xbmc.executebuiltin('Notification(Searching is cancelled,User cancelled search,5000,DefaultIconInfo.png)')

def onClickControlPanelContainer(self, id):
	item = self.getControl(id).getSelectedItem()
	ui = None
	DialogProgress.create("XBMC4Xbox", "Calling TMDB API...")
	if "Movie" in item.getLabel():
		DialogProgress.update(25, 'Fetching info about Movie...')
		entity = service.getInfoAboutMovie(item.getProperty("id"))
		DialogProgress.update(50, 'Fetching actors...')
		actors = service.getActorsForMovie(item.getProperty("id"))
		DialogProgress.update(75, 'Opening Movie...')
		ui = CGUIMovieInfo.CGUIMovieInfo("MovieInfo.xml", utils.getScriptPath(), 'default', entity=entity, actors=actors)

	else:
		DialogProgress.update(25, 'Fetching info about TV Show...')
		entity = service.getInfoAboutTvShow(item.getProperty("id"))
		DialogProgress.update(50, 'Fetching actors...')
		actors = service.getActorsForTvShow(item.getProperty("id"))
		DialogProgress.update(75, 'Opening TV Show...')
		ui = CGUITvShowInfo.CGUITvShowInfo("TvShowInfo.xml", utils.getScriptPath(), 'default', entity=entity, actors=actors)

	ui.doModal()
	del ui