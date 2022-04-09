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
        file_name = file_name[:38].strip() + '.srt'
    return file_name

def writeFile(path, content):
    f = open(path, 'w+')
    f.write(content)
    f.close()
    return path

def getScriptService(id):
    codes = {
        "0": "OpenSubtitles",
        "1": "Titlovi.com"
    }
    return codes[id]

def getScriptLang(id):
    languages = { 
        "0" : "Albanian",
        "1" : "Arabic",
        "2" : "Belarusian",
        "3" : "BosnianLatin",
        "4" : "Bulgarian",
        "5" : "Catalan",
        "6" : "Chinese",
        "7" : "Croatian",
        "8" : "Czech",
        "9" : "Danish",
        "10" : "Dutch",
        "11" : "English",
        "12" : "Estonian",
        "13" : "Finnish",
        "14" : "French",
        "15" : "German",
        "16" : "Greek",
        "17" : "Hebrew",
        "18" : "Hindi",
        "19" : "Hungarian",
        "20" : "Icelandic",
        "21" : "Indonesian",
        "22" : "Italian",
        "23" : "Japanese",
        "24" : "Korean",
        "25" : "Latvian",
        "26" : "Lithuanian",
        "27" : "Macedonian",
        "28" : "Norwegian",
        "29" : "Polish",
        "30" : "Portuguese",
        "31" : "PortugueseBrazil",
        "32" : "Romanian",
        "33" : "Russian",
        "34" : "SerbianLatin",
        "35" : "Slovak",
        "36" : "Slovenian",
        "37" : "Spanish",
        "38" : "Swedish",
        "39" : "Thai",
        "40" : "Turkish",
        "41" : "Ukrainian",
        "42" : "Vietnamese"
    }
    return languages[ id ]

def getScriptOrderBy(id):
    codes = {
        "0": "Language",
        "1": "Download count",
        "2": "Votes",
        "3": "Points",
        "4": "Rating",
        "5": "Upload date",
        "6": "Release"
    }
    return codes[id]

def getSriptOrderDirection(id):
    codes = {
        "0": "Ascending",
        "1": "Descending"
    }
    return codes[id]

#returns Languge Code for given ID
def OSGetLangCode( id ):
    languages = { 
        "None" : "none",
        "Albanian"  	: "sq",
        "Arabic"  	: "ar",
        "Belarusian"  	: "hy",
        "Bosnian"  	: "bs",
        "BosnianLatin": "bs",
        "Bulgarian"  	: "bg",
        "Catalan"  	: "ca",
        "Chinese"  	: "zh",
        "Croatian" 	: "hr",
        "Czech"  		: "cs",
        "Danish" 		: "da",
        "Dutch" 		: "nl",
        "English" 	: "en",
        "Esperanto" 	: "eo",
        "Estonian" 	: "et",
        "Farsi" 		: "fo",
        "Finnish" 	: "fi",
        "French" 		: "fr",
        "Galician" 	: "gl",
        "Georgian" 	: "ka",
        "German" 		: "de",
        "Greek" 		: "el",
        "Hebrew" 		: "he",
        "Hindi" 		: "hi",
        "Hungarian" 	: "hu",
        "Icelandic" 	: "is",
        "Indonesian" 	: "id",
        "Italian" 	: "it",
        "Japanese" 	: "ja",
        "Kazakh" 		: "kk",
        "Korean" 		: "ko",
        "Latvian" 	: "lv",
        "Lithuanian" 	: "lt",
        "Luxembourgish" 	: "lb",
        "Macedonian" 	: "mk",
        "Malay" 		: "ms",
        "Norwegian" 	: "no",
        "Occitan" 	: "oc",
        "Polish" 		: "pl",
        "Portuguese" 	: "pt",
        "PortugueseBrazil" 	: "pb",
        "Brazilian"	: "pb",
        "Romanian" 	: "ro",
        "Russian" 	: "ru",
        "SerbianLatin" 	: "sr",
        "Serbian" 	: "sr",
        "Slovak" 		: "sk",
        "Slovenian" 	: "sl",
        "Spanish" 	: "es",
        "Swedish" 	: "sv",
        "Syriac" 		: "syr",
        "Thai" 		: "th",
        "Turkish" 	: "tr",
        "Ukrainian" 	: "uk",
        "Urdu" 		: "ur",
        "Vietnamese" 	: "vi",
        "English (US)" 	: "en",
        "All" 		: "all"
    }
    return languages[ id ]

def OSGetOrderByCode(id):
    codes = {
        "None": "none",
        "Language": "language",
        "Download count": "download_count",
        "Votes": "votes",
        "Points": "points",
        "Rating": "ratings",
        "Upload date": "upload_date",
        "Release": "release"
    }
    return codes[id]

def OSGetOrderDirectionCode(id):
    codes = {
        "None": "none",
        "Ascending": "asc",
        "Descending": "desc"
    }
    return codes[id]