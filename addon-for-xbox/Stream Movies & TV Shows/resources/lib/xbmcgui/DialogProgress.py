import os, sys
import xbmc, xbmcgui

pDialog = xbmcgui.DialogProgress()

def create(title, info):
    global pDialog
    pDialog.create(title, info)
    pDialog.update(0, info)
    # xbmcgui.lock()

def update(percentage, info):
    global pDialog
    pDialog.update(percentage, info)

def close():
    global pDialog
    pDialog.close()
    # xbmcgui.unlock()

def delete():
    global pDialog
    del pDialog