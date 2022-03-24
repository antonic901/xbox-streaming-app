import os, sys
import xbmc, xbmcgui, xbmcaddon
import resources.lib.utils.utils as utils

__addon__       = xbmcaddon.Addon('script.popcornbox')
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

"""
	Let's say you opened Subtitles script after selecting movie stream. 
	After that 'os' and 'sys' will point to root folder of Subtitles instead 
	of this script even after closing Subtitles script. Which is weird behavior.
	Knowing that, after opening Subtitles script from VideoOSD (when movie playing)
	we can no longer use 'os.getcwd()' when opening new Windows because he will 
	look for '.XML' files in Subtitles folder instead of this script. So workaround is to
	save  path to this script on global variable which can be accessed from everywhere in code.
"""
utils.setScriptPath(os.getcwd())

if (__name__ == "__main__"):
	this = '__main__->'
	
	log('==================================')
	log('initializing...')
	log('Addon Id	: %s' % __addon_id__)
	log('Addon Icon	: %s' % __addon_ico__)
	log('Addon Ver.	: %s' % __addon_ver__)
	log('Language	: %s' % __language__)
	log('==================================')

	#check is configuration file created
	if os.path.isfile(__cwd__ + "\\configuration.json"):
		print ("Configuration file is found!")

	else:
		#if not found, promt user to create one
		import resources.lib.gui.CGUISettings as CGUISettings
		ui = CGUISettings.CGUISettings('_Settings.xml', __cwd__, 'default', allow_cancel=False)
		ui.doModal()
		del ui

	import resources.lib.gui.CGUIMain as __init__
	ui = __init__.CGUIMain('Main.xml', __cwd__, 'default')
	ui.doModal()

	try:
		del ui
	except:
		log("UI is already deleted.")

	log('terminating...')
	log('==================================')