import os, sys
import xbmc, xbmcgui

pDialog = xbmcgui.DialogProgress()

def create(title, info):
    global pDialog
    pDialog.create(title, info)
    pDialog.update(0, info)

def update(percentage, info):
    global pDialog
    pDialog.update(percentage, info)

def close():
    global pDialog
    pDialog.close()

def iscanceled():
    global pDialog
    return pDialog.iscanceled()



def delete():
    global pDialog
    del pDialog