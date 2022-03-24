import os, sys
import xbmc, xbmcgui

import requests
import utils

API = "https://api.opensubtitles.com/api/v1/{}"
token = "YOUR_TOKEN"

DOWNLOAD_PATH = "E:\Subtitles"

headers = {
    "Accept": "application/json",
    "Api-Key": "YOUR_API_KEY",
    "Content-Type": "application/json",
    "Authorization": token
}

params = {
    "languages": "sr,bs,hr",
    "order_by": "download_count",
    "order_direction": "desc"
}

def search(meta):
    if meta['imdb_id'] != '': params['imdb_id'] = meta['imdb_id']
    if meta['tmdb_id'] != '': params['tmdb_id'] = meta['tmdb_id']
    if meta['title'] and meta['year'] != 0: params['query'] = "{} {}".format(meta['title'], meta['year'])
    if meta['episode'] != '': params['episode_number'] = meta['episode']
    if meta['season'] != '': params['season_number'] = meta['season']

    if len(params) > 3:
        return createListItems(sendRequest("subtitles", headers, params, None).data)
        
    else:
        # TODO Extract name, year, season and episode if they are presented from file name
        # TODO Search by query. For TV Show (name + s0x + e0x). For Movie (name + year)
        return []

def manualSearch(query):
    params['query'] = query
    return createListItems(sendRequest("subtitles", headers, params, None).data)

def getDownloadLink(id):
    data = sendRequest("download", headers, None, {"file_id":id})

    return data.link, data.file_name 

def downloadSubtitle(download_link, file_name):
    response = requests.get(download_link, headers={'Content-Type':'application/json'})

    if response.status_code != 200:
        xbmc.executebuiltin('Notification(OpenSubtitles API returned %s,%s,5000,DefaultIconInfo.png)' % (response.status_code, response.text))
        return None

    # xbox have limit od 42 characters
    file_name = utils.renameFile(file_name)

    return utils.writeFile(os.path.join(DOWNLOAD_PATH, file_name), response.text)

def sendRequest(action, headers, params, json):
    if "download" in action:
        response = requests.post(API.format(action), headers=headers, params=params, json=json)
    else :
        response = requests.get(API.format(action), headers=headers, params=params, json=json)

    if response.status_code != 200:
        xbmc.executebuiltin('Notification(OpenSubtitles API returned %s,%s,5000,DefaultIconInfo.png)' % (response.status_code, response.text))
        return []

    return utils.createObject(response.text)

def createListItems(subtitles):
    listitems = []
    for subtitle in subtitles:
        item = xbmcgui.ListItem('Subtitle')
        item.setProperty('id', subtitle.id)
        item.setProperty('language', subtitle.attributes.language)
        item.setProperty('download_count', subtitle.attributes.download_count)
        item.setProperty('uploader', subtitle.attributes.uploader.name)
        item.setProperty('release', subtitle.attributes.release)
        item.setProperty('file_id', subtitle.attributes.files[0].file_id)
        listitems.append(item)

    return listitems