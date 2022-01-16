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
		createRightMenu(self)
		# xbmc.sleep(100)
		self.setFocusId(34000)

		self.control_id_label1 = 34002
		self.control_id_label2 = 34100
		self.control_id_label3 = 34101
		self.control_id_label4 = 34102
		self.control_id_label5 = 34103

	def onAction(self, action):
		if action in self.action_exitkeys_id:
			self.close()

	def onFocus(self, controlId):
		pass

	def onClick(self, id):
		if id == self.control_id_menu:
			item = self.control_menu.getSelectedItem()
			if "Movies" == item.getLabel():
				getMoviesForHomeScreen(self)
				self.getControl(self.control_id_label1).setLabel(item.getLabel())
				changeLabelsForPanels(self, 'In Theatres', 'Popular Movies', 'Upcoming Movies', 'Top Rated')
			elif "TV Shows" == item.getLabel():
				getTvShowsForHomeScreen(self)
				self.getControl(self.control_id_label1).setLabel(item.getLabel())
				changeLabelsForPanels(self, 'On The Air', 'Popular TV Shows', 'Airing Today', 'Top Rated')
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

def createRightMenu(self):
		self.control_id_panel_in_theatres = 34200
		self.control_id_panel_popular = 34201
		self.control_id_panel_upcoming = 34202
		self.control_id_panel_top_rated = 34203

		self.control_panel_in_theatres = self.getControl(self.control_id_panel_in_theatres)
		self.control_panel_popular = self.getControl(self.control_id_panel_popular)
		self.control_panel_upcoming = self.getControl(self.control_id_panel_upcoming)
		self.control_panel_top_rated = self.getControl(self.control_id_panel_top_rated)

		getMoviesForHomeScreen(self)

def changeLabelsForPanels(self, label2, label3, label4, label5):
	self.getControl(self.control_id_label2).setLabel(label2)
	self.getControl(self.control_id_label3).setLabel(label3)
	self.getControl(self.control_id_label4).setLabel(label4)
	self.getControl(self.control_id_label5).setLabel(label5)

def clearAllListItems(self):
	self.control_panel_in_theatres.reset()
	self.control_panel_popular.reset()
	self.control_panel_upcoming.reset()
	self.control_panel_top_rated.reset()

#called when 'Movies' button is pressed
def getMoviesForHomeScreen(self):
	clearAllListItems(self)

	movies_in_theatres = service.getMoviesInTheatres(1)
	for movie in movies_in_theatres:
		item = xbmcgui.ListItem(movie.title, movie.release_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
		item.setProperty('rating', movie.vote_average)
		self.control_panel_in_theatres.addItem(item)

	popular_movies = service.getPopularMovies(1)
	for movie in popular_movies:
		item = xbmcgui.ListItem(movie.title, movie.release_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
		item.setProperty('rating', movie.vote_average)
		self.control_panel_popular.addItem(item)

	upcoming_movies = service.getUpcomingMovies(1)
	for movie in upcoming_movies:
		item = xbmcgui.ListItem(movie.title, movie.release_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
		item.setProperty('rating', movie.vote_average)
		self.control_panel_upcoming.addItem(item)

	top_rated_movies = service.getTopRatedMovies(1)
	for movie in top_rated_movies:
		item = xbmcgui.ListItem(movie.title, movie.release_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
		item.setProperty('rating', movie.vote_average)
		self.control_panel_top_rated.addItem(item)

#called when 'TV Shows' button is pressed
def getTvShowsForHomeScreen(self):
	clearAllListItems(self)

	movies_in_theatres = service.getOnTheAirTvShows(1)
	for movie in movies_in_theatres:
		item = xbmcgui.ListItem(movie.name, movie.first_air_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
		item.setProperty('rating', movie.vote_average)
		self.control_panel_in_theatres.addItem(item)

	popular_movies = service.getPopularTvShows(1)
	for movie in popular_movies:
		item = xbmcgui.ListItem(movie.name, movie.first_air_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
		item.setProperty('rating', movie.vote_average)
		self.control_panel_popular.addItem(item)

	upcoming_movies = service.getAiringTodayTvShows(1)
	for movie in upcoming_movies:
		item = xbmcgui.ListItem(movie.name, movie.first_air_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
		item.setProperty('rating', movie.vote_average)
		self.control_panel_upcoming.addItem(item)

	top_rated_movis = service.getTopRatedTvShows(1)
	for movie in top_rated_movis:
		item = xbmcgui.ListItem(movie.name, movie.first_air_date, iconImage=movie.poster_path, thumbnailImage=movie.poster_path)
		item.setProperty('rating', movie.vote_average)
		self.control_panel_top_rated.addItem(item)