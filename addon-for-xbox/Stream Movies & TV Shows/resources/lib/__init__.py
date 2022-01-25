import os, sys
import xbmc
import xbmcgui
import service
import CGUISearch, CGUIMovieInfo, CGUITvShowInfo

class GUI(xbmcgui.WindowXML):

	def __init__(self, *args, **kwargs):
		self.__cwd__ = kwargs['__cwd__']
		xbmcgui.WindowXML.__init__(self, *args, **kwargs)

	def onInit(self):
		self.action_exitkeys_id = [10, 92]
		assignIDs(self)
		createLeftMenu(self)
		getMoviesForHomeScreen(self)
		xbmc.sleep(1000)
		self.setFocusId(34000)

	def onAction(self, action):
		if action in self.action_exitkeys_id:
			self.close()

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
	self.control_id_panel_in_theatres = 34200
	self.control_id_panel_popular = 34201
	self.control_id_panel_upcoming = 34202
	self.control_id_panel_top_rated = 34203

	self.control_id_label1 = 34002
	self.control_id_label2 = 34100
	self.control_id_label3 = 34101
	self.control_id_label4 = 34102
	self.control_id_label5 = 34103

def createLeftMenu(self):
		self.control_id_menu = 34000
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

def clearAllListItems(self):
	self.getControl(self.control_id_panel_in_theatres).reset()
	self.getControl(self.control_id_panel_popular).reset()
	self.getControl(self.control_id_panel_upcoming).reset()
	self.getControl(self.control_id_panel_top_rated).reset()

def populateContainer(self, id, items):
	container = self.getControl(id)
	container.reset()
	for item in items:
		container.addItem(item)

#called when 'Movies' button is pressed
def getMoviesForHomeScreen(self):
	populateContainer(self, self.control_id_panel_in_theatres, service.getMoviesInTheatres(1))
	populateContainer(self, self.control_id_panel_popular, service.getPopularMovies(1))
	populateContainer(self, self.control_id_panel_upcoming, service.getUpcomingMovies(1))
	populateContainer(self, self.control_id_panel_top_rated, service.getTopRatedMovies(1))

#called when 'TV Shows' button is pressed
def getTvShowsForHomeScreen(self):
	populateContainer(self, self.control_id_panel_in_theatres, service.getOnTheAirTvShows(1))
	populateContainer(self, self.control_id_panel_popular, service.getPopularTvShows(1))
	populateContainer(self, self.control_id_panel_upcoming, service.getAiringTodayTvShows(1))
	populateContainer(self, self.control_id_panel_top_rated, service.getTopRatedTvShows(1))

#Called when 'Search" button is pressed
def onClickControlPanelMenu(self):
	item = self.control_menu.getSelectedItem()
	if "Movies" == item.getLabel():
		getMoviesForHomeScreen(self)
		self.getControl(self.control_id_label1).setLabel(item.getLabel())
		changeLabelsForPanels(self, 'In Theatres', 'Popular Movies', 'Upcoming Movies', 'Top Rated')
	elif "TV Shows" == item.getLabel():
		getTvShowsForHomeScreen(self)
		self.getControl(self.control_id_label1).setLabel(item.getLabel())
		changeLabelsForPanels(self, 'On The Air', 'Popular TV Shows', 'Airing Today', 'Top Rated')
	elif "Search Movi" in item.getLabel():
		keyboard = xbmc.Keyboard()
		keyboard.doModal()
		keyboardConfirmed = keyboard.isConfirmed()
		enteredText = keyboard.getText()
		del keyboard
		if(keyboardConfirmed and enteredText != ""):		
			movies = service.searchMovies(enteredText, 1)
			if movies:
				ui = CGUISearch.CGUISearch('search.xml', self.__cwd__, 'default', __cwd__=self.__cwd__, query=enteredText, type='Movies', items=movies)
				ui.doModal()
				del ui
		else:
			xbmc.executebuiltin('Notification(Searching is cancelled,User cancelled search,5000,DefaultIconInfo.png)')
	elif "Search TV" in item.getLabel():
		keyboard = xbmc.Keyboard()
		keyboard.doModal()
		keyboardConfirmed = keyboard.isConfirmed()
		enteredText = keyboard.getText()
		del keyboard
		if(keyboardConfirmed and enteredText != ""):
			tv_shows = service.searchTvShows(enteredText, 1)
			ui = CGUISearch.CGUISearch('search.xml', self.__cwd__, 'default', __cwd__=self.__cwd__, query=enteredText, type='TV Shows', items=tv_shows)
			ui.doModal()
			del ui
		else:
			xbmc.executebuiltin('Notification(Searching is cancelled,User cancelled search,5000,DefaultIconInfo.png)')

def onClickControlPanelContainer(self, id):
	item = self.getControl(id).getSelectedItem()
	entity = []
	actors = []
	ui = None
	if "Movie" in item.getLabel():
		entity = service.getInfoAboutMovie(item.getProperty("id"))
		actors = service.getActorsForMovie(item.getProperty("id"))
		ui = CGUIMovieInfo.CGUIMovieInfo("movieInfo.xml", self.__cwd__, 'default', __cwd__=self.__cwd__, entity=entity, actors=actors)
	else:
		entity = service.getInfoAboutTvShow(item.getProperty("id"))
		actors = service.getActorsForTvShow(item.getProperty("id"))
		ui = CGUITvShowInfo.CGUITvShowInfo("tvShowInfo.xml", self.__cwd__, 'default', __cwd__=self.__cwd__, entity=entity, actors=actors)
	ui.doModal()
	del ui