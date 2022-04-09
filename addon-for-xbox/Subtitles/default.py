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
		_settings_ = xbmc.Settings(path=os.getcwd())
		_settings_.openSettings()

	else:
		item = xbmc.Player().getVideoInfoTag()
		meta = {
			"imdb_id": item.getDirector(),
			"tmdb_id": item.getTagLine(),
			# "tmdb_id": "634649",
			"title": item.getTitle(),
			"year": item.getYear(),
			"season": item.getGenre(),
			# "season": "1",
			"episode": item.getPlot()
			# "episode": "1"
		}

		from GUIMain import GUIMain

		if not xbmc.getCondVisibility('Player.Paused') : 
			xbmc.Player().pause()

		ui = GUIMain("_main.xml", os.getcwd(), "Default", meta=meta)
		ui.doModal()
		del ui

		xbmc.Player().pause()