import os, sys
import xbmc, xbmcgui
import json
from resources.lib.utils import utils

class CGUISettings(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        self.path = "%s\\configuration.json" % utils.getScriptPath()
        if os.path.isfile(self.path):
            print ("Configuration file is found! Reading...")
            with open(self.path) as configuration_file:
                self.dict = json.load(configuration_file)
                configuration_file.close()
        else:
            print ("Configuration file is not found! Creating one...")
            f = open(self.path, 'w+')
            conf = '{"HOST_ADDRESS":"","PORT":"","API":"http://api.themoviedb.org/3","API_KEY":"f0d9239acde293e5222746bf11d1a3dc"}'
            f.write(conf)
            f.close()

            print ("Configuration file is created. Reading from it...")

            with open(self.path) as configuration_file:
                self.dict = json.load(configuration_file)
                configuration_file.close()

        self.allowCancel = kwargs['allow_cancel']
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        assingIDs(self)
        createMenu(self)
        self.setFocusId(self.cPanel)

    def onAction(self, action):
        if action in self.action_exitkeys_id:
            if self.allowCancel is True:
                self.close()
            else:
                xbmc.executebuiltin('Notification(Settings,Please complete first time setup,5000,DefaultIconInfo.png)')

    def onFocus(self, controlId):
        pass

    def onClick(self, id):
        if id == self.cSaveButton:
            # TODO Implement saving configs
            for key, value in self.dict.items():
                if value in ['', None]:
                    xbmc.executebuiltin('Notification(Settings,%s is not valid!,5000,DefaultIconInfo.png)' % key)
                    return
            
            print ("Updating configuration file...")
            with open(self.path, "w+") as configuration:
                json.dump(self.dict, configuration)
                configuration.close()
            
            print ("Configuration file is updated!")

            xbmc.executebuiltin('Notification(Settings,Settings are saved,5000,DefaultIconInfo.png)')
            self.close()

        elif id == self.cPanel:
            item = self.getControl(id).getSelectedItem()

            enteredText = ''
            if item.getProperty('isHostAddress'):
                keyboard = xbmcgui.Dialog()
                enteredText = keyboard.numeric(3, 'Please enter Host Address')
                del keyboard

            elif item.getProperty('isPort'):
                keyboard = xbmcgui.Dialog()
                enteredText = keyboard.numeric(0, 'Please enter port')
                del keyboard

            else:
                keyboard = xbmc.Keyboard()
                keyboard.doModal()
                enteredText = keyboard.getText()
                del keyboard

            if enteredText not in [None, '']:
                item.setLabel2(enteredText)
                self.dict[item.getLabel()] = enteredText

            else:
                xbmc.executebuiltin('Notification(Cancelled input,User cancelled input,5000,DefaultIconInfo.png)')

def createMenu(self):
    cPanel = self.getControl(self.cPanel)
    cPanel.reset()

    for key, value in self.dict.items():
        item = xbmcgui.ListItem(key, value)

        # sets property to know which type of keyboard to open
        if 'HOST' in key:
            item.setProperty('isHostAddress', True)

        elif 'PORT' in key:
            item.setProperty('isPort', True)

        cPanel.addItem(item)

def assingIDs(self):
    self.action_exitkeys_id = [10, 92]
    self.cPanel = 34000
    self.cSaveButton = 4000