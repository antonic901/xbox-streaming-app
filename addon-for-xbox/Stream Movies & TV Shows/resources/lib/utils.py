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