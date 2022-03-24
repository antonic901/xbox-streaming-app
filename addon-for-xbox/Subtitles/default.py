import os, sys
import xbmc, xbmcgui

BASE_RESOURCE_PATH = xbmc.translatePath( os.path.join( os.getcwd(), 'resources', 'lib' ) )
sys.path.append (BASE_RESOURCE_PATH)

def log( msg ):
	print ('::Subtitles:Default: ' + msg)
	message = '::Subtitles:Default:%s' % msg
	xbmc.log(msg=message, level=xbmc.LOGDEBUG)

if (__name__ == "__main__"):
	log('==================================')
	log('initializing...')
	log('Addon Id	: %s' % 'script.subtitles')
	log('Language	: %s' % xbmc.getLanguage())
	log('==================================')

	if not xbmc.Player().isPlayingVideo():
		xbmc.executebuiltin('Notification(Subtitles,Settings are in development.,5000,DefaultIconInfo.png)')
		# from GUISettings import GUISettings
		# ui = GUISettings("_settings.xml", os.getcwd(), "Default")
		# ui.doModal()
		# del ui
	
	else:
		item = xbmc.Player().getVideoInfoTag()
		meta = {
			"imdb_id": item.getDirector(),
			"tmdb_id": item.getTagLine(),
			# "tmdb_id": "696806",
			"title": item.getTitle(),
			"year": item.getYear(),
			"season": item.getGenre(),
			# "season": "1",
			"episode": item.getPlot()
			# "episode": "1"
		}

		print meta

		from GUIMain import GUIMain

		if not xbmc.getCondVisibility('Player.Paused') : 
			xbmc.Player().pause()

		ui = GUIMain("_main.xml", os.getcwd(), "Default", meta=meta)
		ui.doModal()
		del ui

		xbmc.Player().pause()