import os, sys
import xbmc, xbmcgui, xbmcaddon

__addon__       = xbmcaddon.Addon()
__addon_id__    = __addon__.getAddonInfo('id')
__addon_ver__ 	= __addon__.getAddonInfo('version')
__addon_ico__ 	= __addon__.getAddonInfo('icon')
__language__	= xbmc.getLanguage()
__cwd__			= __addon__.getAddonInfo('path').decode('utf-8')
__its_xbox__ 	= xbmc.getCondVisibility( 'System.Platform.Xbox' )

def log( msg ):
	print ('::Streaming:Default: ' + msg)
	message = '::Streaming:Default:%s' % msg
	xbmc.log(msg=message, level=xbmc.LOGDEBUG)

if (__name__ == "__main__"):
	this = '__main__->'
		
	log('==================================')
	log('initializing...')
	log('Addon Id	: %s' % __addon_id__)
	log('Addon Icon	: %s' % __addon_ico__)
	log('Addon Ver.	: %s' % __addon_ver__)
	log('Language	: %s' % __language__)
	log('==================================')

	import resources.lib.gui.CGUIMain as __init__
	ui = __init__.CGUIMain('main.xml', __cwd__, 'default', __cwd__=__cwd__)
	ui.doModal()
	del ui