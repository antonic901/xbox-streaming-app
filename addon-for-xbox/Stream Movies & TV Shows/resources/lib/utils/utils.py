import os, sys
import json

script_path = None

def setScriptPath(path):
    global script_path
    script_path = path

def getScriptPath():
    global script_path
    return script_path

def createObject(jsonObject):    
    class Generic:
        @classmethod
        def from_dict(cls, dict):
            obj = cls()
            obj.__dict__.update(dict)
            return obj

    return json.loads(jsonObject, object_hook=Generic.from_dict)

def populateContainer(self, id, items):
	container = self.getControl(id)
	container.reset()
	for item in items:
		container.addItem(item)

def convertTo(unit, input):
    base = 1024
    if unit in ['KB', 'kb']:
        return input / base
    base = base * 1024
    if unit in ['MB', 'mb']:
        return input / base
    base = base * 1024
    if unit in ['GB', 'gb']:
        return input / base
    base = base * 1024
    if unit in ['TB', 'tb']:
        return input / base
    else:
        return input