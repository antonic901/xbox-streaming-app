import os, sys
import xbmcgui, xbmcaddon

__addon__       = xbmcaddon.Addon()
__addon_id__    = __addon__.getAddonInfo('id')
__addon_ver__ 	= __addon__.getAddonInfo('version')
__addon_ico__ 	= __addon__.getAddonInfo('icon')
__language__	= xbmc.getLanguage()
__cwd__			= __addon__.getAddonInfo('path').decode('utf-8')
# __resources__	= xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib').encode('utf-8') ).decode('utf-8')
__its_xbox__ 	= xbmc.getCondVisibility( 'System.Platform.Xbox' )

# sys.path.append( __resources__ )

def log( msg ):
	print '::Streaming:Default:%s' % msg
	message = '::Streaming:Default:%s' % msg
	xbmc.log(msg=message, level=xbmc.LOGDEBUG)

# getLocalizedString = __addon__.getLocalizedString
# getSetting = __addon__.getSetting

if (__name__ == "__main__"):
	this = '__main__->'
		
	log('==================================')
	log('initializing...')
	log('Addon Id	: %s' % __addon_id__)
	log('Addon Icon	: %s' % __addon_ico__)
	log('Addon Ver.	: %s' % __addon_ver__)
	log('Language	: %s' % __language__)
	log('==================================')
	
	import resources.lib.__init__ as __init__
	ui = __init__.GUI('main.xml', __cwd__, 'default')
	ui.doModal()
	del ui
	