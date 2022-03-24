import os, sys
import json

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

def renameFile(file_name):
    if len(file_name) > 42:
        file_name = file_name[:38] + '.srt'
    return file_name

def writeFile(path, content):
    f = open(path, 'w+')
    f.write(content)
    f.close()
    return path