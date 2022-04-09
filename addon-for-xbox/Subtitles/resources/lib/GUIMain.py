import os, sys
import xbmc, xbmcgui

import DialogProgress
import opensubtitles
import utils

print(os.getcwd())

_settings_ = xbmc.Settings(path=os.getcwd())

class GUIMain(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        self.meta = kwargs['meta']
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        assignIDs(self)
        createServices(self)
        self.setFocusId(130)
        DialogProgress.create('XBMC4Xbox', 'Searching subtitles...')
        subtitles = callDefaultService(self.meta)
        DialogProgress.update(50, 'Loading subtitles...')
        utils.populateContainer(self, self.cSubtitlesId, subtitles)
        DialogProgress.update(90, 'Finishing...')
        xbmc.sleep(2000)
        DialogProgress.close()

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            # DialogProgress.delete()
            self.close()

    def onFocus(self, id):
        pass

    def onClick(self, id):
        if id == self.cServicesId:
            item = self.getControl(id).getSelectedItem()
            if 'OpenSubtitles' in item.getLabel():
                DialogProgress.create('XBMC4Xbox', 'Searching subtitles...')
                subtitles = opensubtitles.search(self.meta)
                DialogProgress.update(50, 'Loading subtitles...')
                utils.populateContainer(self, self.cSubtitlesId, subtitles)
                DialogProgress.update(90, 'Finishing...')
                xbmc.sleep(2000)
                DialogProgress.close()

            else:
                xbmc.executebuiltin('Notification(Subtitles,Titlovi.com are under development,5000,DefaultIconInfo.png)')

        elif id == self.cSubtitlesId:
            item = self.getControl(id).getSelectedItem()
            DialogProgress.create('XBMC4Xbox', 'Calling OpenSubtitles API...')
            DialogProgress.update(25, 'Finding download link...')
            download_link, file_name = opensubtitles.getDownloadLink(item.getProperty("file_id"))

            if download_link != None:
                DialogProgress.update(50, 'Downloading subtitle...')
                subtitle_path = opensubtitles.downloadSubtitle(download_link, file_name)
                if subtitle_path != None:
                    DialogProgress.update(75, 'Loading subtitle...')
                    xbmc.Player().setSubtitles(subtitle_path)

            DialogProgress.update(99, 'Finishing...')
            xbmc.sleep(2000)
            DialogProgress.close()
            self.close()
        
        elif id == self.cManualSearch:
            keyboard = xbmc.Keyboard()
            keyboard.doModal()
            keyboardConfirmed = keyboard.isConfirmed()
            enteredText = keyboard.getText()
            del keyboard

            if keyboardConfirmed and enteredText != '':
                item = self.getControl(self.cServicesId).getSelectedItem()
                if 'OpenSubtitles' in item.getLabel():
                    DialogProgress.create('XBMC4Xbox', 'Searching subtitles...')
                    subtitles = opensubtitles.manualSearch(enteredText)
                    DialogProgress.update(50, 'Loading subtitles...')
                    utils.populateContainer(self, self.cSubtitlesId, subtitles)
                    DialogProgress.update(90, 'Finishing...')
                    xbmc.sleep(2000)
                    DialogProgress.close()

                else:
                    xbmc.executebuiltin('Notification(Subtitles,Titlovi.com are under development,5000,DefaultIconInfo.png)')
            
            else:
                xbmc.executebuiltin('Notification(Searching is cancelled,User cancelled search,5000,DefaultIconInfo.png)')

def callDefaultService(meta):
    subtitles = []
    if "OpenSubtitles" in utils.getScriptService(_settings_.getSetting("defservice")):  
        subtitles = opensubtitles.search(meta)

    else:
        xbmc.executebuiltin('Notification(Subtitles,{} are under development,5000,DefaultIconInfo.png)'.format(_settings_.getSetting("defservice")))

    return subtitles

def assignIDs(self):
    self.action_exitkeys_id = [10, 92]

    self.cServicesId = 120
    self.cSubtitlesId = 130
    self.cManualSearch = 4000

def createServices(self):
    self.cServices = self.getControl(self.cServicesId)
    listitems = [
        xbmcgui.ListItem('OpenSubtitles', iconImage='icons/32/movies.png'), 
        xbmcgui.ListItem('Titlovi.com', iconImage='icons/32/tvshows.png')
    ]
    self.cServices.reset()
    for item in listitems:
        self.cServices.addItem(item)