import sys
import os
import xbmc
import xbmcgui
import osdb
from osdb import OSDBServer
from utilities import *
import urllib
import unzip
import xmlrpclib
import time
import base64
import zipfile
import re
from urllib2 import Request, urlopen, URLError, HTTPError
import unicodedata
import stat
import shutil
_ = sys.modules[ "__main__" ].__language__
__scriptname__ = sys.modules[ "__main__" ].__scriptname__
__version__ = sys.modules[ "__main__" ].__version__
__settings__ = xbmc.Settings( path=os.getcwd() )

STATUS_LABEL = 100
LOADING_IMAGE = 110
SUBTITLES_LIST = 120

def timeout(func, args=(), kwargs={}, timeout_duration=10, default=None):

    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = "000000000000"
        def run(self):
            self.result = func(*args, **kwargs)
    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return it.result
    else:
        return it.result


class GUI( xbmcgui.WindowXMLDialog ):
        
    def __init__( self, *args, **kwargs ):
        pass
          
    def set_session(self,session_id):
        self.session_id = session_id

    def set_allparam(self, path,search,temp,sub_folder, year,debug):
        self.debug = debug                                            # debug?
        self.year = year                                              # Year
                
        lang1 = toScriptLang(__settings__.getSetting( "Language1" ))  # Full language 1
        lang2 = toScriptLang(__settings__.getSetting( "Language2" ))  # Full language 2  
        lang3 = toScriptLang(__settings__.getSetting( "Language3" ))  # Full language 2
        
        self.lang1 = toOpenSubtitlesId( lang1 )                       # 2 letter language 1
        self.lang_two1 = toOpenSubtitles_two(lang1)                   # 3 letter language 1
        
        
        self.lang2 = toOpenSubtitlesId( lang2 )                       # 2 letter language 2
        self.lang_two2 = toOpenSubtitles_two(lang2)                   # 3 letter language 2
        
        self.lang3 = toOpenSubtitlesId( lang3 )                       # 2 letter language 3
        self.lang_two3 = toOpenSubtitles_two(lang3)                   # 3 letter language 3
        
                
        self.sub_folder = sub_folder                                  # Subtitle download folder
        
        self.file_original_path = urllib.unquote ( path )             # Movie Path

        self.file_path = urllib.unquote( path )
        
        self.set_temp = temp
        
        self.search_string1 = unicode(search, 'utf-8')                # de-accent Search String
        self.search_string = unicodedata.normalize('NFKD', unicode(self.search_string1)).encode('ascii','ignore')

        if (__settings__.getSetting( "fil_name" ) == "true"):         # Display Movie name or search string
            self.file_name = os.path.basename( path )
        else:
            self.file_name = self.search_string.replace("+"," ")
            if self.year != 0 and self.year != "" : self.file_name = self.file_name + " (" + str(self.year) + ")"
          


#### ---------------------------- Set Service ----------------------------###     

        self.service = ""
        self.OS =  __settings__.getSetting( "OS" ) == "true"
        if self.OS and ( __settings__.getSetting( "defservice") == "2") : self.service = "OpenSubtitles"

        self.PN =  __settings__.getSetting( "PN" ) == "true"
        self.username = __settings__.getSetting( "PNuser" )
        self.password = __settings__.getSetting( "PNpass" )
        if self.PN and len(self.username) > 1 and len(self.password) >1 :
            if ( __settings__.getSetting( "defservice") == "1"):
                self.service = "Podnapisi"
        else: 
            self.PN = False

        if self.service == "" :
            if self.PN and len(self.username) > 1 and len(self.password) >1 :
                self.service = "Podnapisi"
            else:   
                self.PN = False
              
            if self.OS:
                self.service = "OpenSubtitles"
                      
        if not self.OS and not self.PN:
            import xbmcgui
            dialog = xbmcgui.Dialog()
            possibleChoices = ["OpenSubtitles","Podnapisi"]  
            choice = dialog.select( _( 505 ) , possibleChoices)
            self.service = ""
            if choice == 0:
                self.service = "OpenSubtitles"
                self.OS = True
            if choice == 1:
                if len(self.username) > 1 and len(self.password) >1 :
                    self.service = "Podnapisi"
                    self.PN = True
                else:   
                    dialog = xbmcgui.Dialog()
                    selected = dialog.ok("OpenSubtitles_OSD", "Podnapisi service requires username and password", "Register at www.podnapisi.net and enter it", "in script settings menu" )                         
                    __settings__.openSettings()
                    self.username = __settings__.getSetting( "PNuser" )
                    self.password = __settings__.getSetting( "PNpass" )
                    if len(self.username) > 1 and len(self.password) >1 :
                        self.PN = True
                        self.service = "Podnapisi"
                    else:
                        return -1       

#### ---------------------------- end set Service ----------------------------###         


        self.mansearch =  __settings__.getSetting( "searchstr" ) == "true" # Manual search string??
        self.list = []
        self.pos = -1
                
        if self.OS : self.pos = self.pos +1
        if self.PN : self.pos = self.pos +1
        service_num = self.pos
        if self.mansearch : self.pos = self.pos +1
        
        
        if self.debug : ## Debug?
                
            LOG( LOG_INFO, "Manual Search : [%s]" , self.mansearch )
            LOG( LOG_INFO, "Service : [%s]" , self.service )
            LOG( LOG_INFO, "PN Service : [%s]" , self.PN )
            LOG( LOG_INFO, "OS Service : [%s]" , self.OS )
            LOG( LOG_INFO, "Search String: [%s]" , self.search_string )
            LOG( LOG_INFO, "Temp?: [%s]" ,  self.set_temp )
            LOG( LOG_INFO, "File Path: [%s]" ,  self.file_path )
            LOG( LOG_INFO, "Year: [%s]" ,  str(self.year) )
            LOG( LOG_INFO, "Subtitle Folder: [%s]" ,  self.sub_folder )
            LOG( LOG_INFO, "Language 1: [%s]" ,  self.lang1  )
            LOG( LOG_INFO, "Language 2: [%s]" ,  self.lang2  )
            LOG( LOG_INFO, "Language 3: [%s]" ,  self.lang3  )      
        
        return service_num
          
          

#### ---------------------------- End Set All ----------------------------###


    def set_filehash(self):
        
        hashFile(self.file_original_path)
        self.file_hash = hashFile(self.file_original_path)
        if self.debug : LOG( LOG_INFO, "File Hash: [%s]" , ( self.file_hash ) )
        return self.file_hash
                
    def set_filesize( self, size ):
        if self.debug : LOG( LOG_INFO, "File Size: [%s]" , ( size ) )
        self.file_size = size


    def set_subtitles( self, subtitles ):
        self.subtitles = subtitles

    def onInit( self ):
        if self.debug : LOG( LOG_INFO, "onInit" )
        self.setup_all()

            
    
    def setup_all( self ):
        self.getControl( 300 ).setLabel( _( 601 ) )
        self.getControl( 301 ).setLabel( _( 602 ) )
        self.setup_variables()
        self.connect()

        
    def setup_variables( self ):
        try: xbox = xbmc.getInfoLabel( "system.xboxversion")
        except:xbox = ""
        if xbox == "":
            self.set_xbox = False
        else:
            self.set_xbox = True
            if self.debug : LOG( LOG_INFO, "XBOX detected" )
        self.controlId = -1
        self.osdb_server = OSDBServer()
        self.manuall = False
    
    
    def connect( self ):
        self.getControl( SUBTITLES_LIST ).reset()
        self.osdb_server.Create(self.debug)

        if self.service == "OpenSubtitles":
            self.getControl( 111 ).setVisible( False )
            self.getControl( 110 ).setVisible( True )
            self.connected = True
            self.getControl( STATUS_LABEL ).setLabel( _( 635 ) )
            self.search_subtitles()

        if self.service == "Podnapisi":
            self.getControl( 110 ).setVisible( False )
            self.getControl( 111 ).setVisible( False )
            self.getControl( STATUS_LABEL ).setLabel( _( 646 ) )
            self.search_subtitles_pod()
        

###-------------------------- OS search -------------################

    def search_subtitles( self ):

        self.getControl( STATUS_LABEL ).setLabel( _( 646 ) )    

        ok = False
        msg = ""
        
        if self.file_original_path.find("http") > -1 or self.set_xbox == True : 
           hash_search = False
        else:
           hash_search = True
        
        try:
           if hash_search :
               hashTry = timeout(self.set_filehash, timeout_duration=5)
               if self.debug : LOG( LOG_INFO, "Search by hash and name " +  os.path.basename( self.file_original_path ) )
               self.getControl( STATUS_LABEL ).setLabel( _( 642 ) % ( "...", ) )
               
               self.set_filesize ( os.path.getsize( self.file_original_path ) )
                  
               try : ok,msg = self.osdb_server.searchsubtitles( self.search_string, hashTry,self.file_size,self.lang1,self.lang2,self.lang3,self.year,hash_search )
               except: self.connected = False

               if self.debug : LOG( LOG_INFO, "Hash and Name Search: " + msg )
               
           else: 
               if self.debug : LOG( LOG_INFO, "Search by Name " + self.file_original_path )
               self.getControl( STATUS_LABEL ).setLabel( _( 642 ) % ( "...", ) )
                
               try : ok,msg = self.osdb_server.searchsubtitles( self.search_string, "000000000" ,"000000000",self.lang1,self.lang2,self.lang3,self.year,hash_search )
               except: self.connected = False
               if self.debug : LOG( LOG_INFO, "Name Search: " + msg )
               

               
           self.osdb_server.mergesubtitles()
           if not ok: self.getControl( STATUS_LABEL ).setLabel( _( 634 ) % ( msg, ) )

           label = ""
           self.list = []
           if self.PN :
               label2 = "[COLOR=FFFF0000]%s[/COLOR]" % (  _( 610 ) + "Podnapisi.net" )
               listitem = xbmcgui.ListItem( label,label2 )
               self.list.append("PN")
               self.getControl( SUBTITLES_LIST ).addItem( listitem )
           if self.mansearch :
               label2 = "[COLOR=FF00FF00]%s[/COLOR]" % (  _( 612 ) )
               listitem = xbmcgui.ListItem( label,label2 )
               self.list.append("MN")
               self.getControl( SUBTITLES_LIST ).addItem( listitem )
           if self.osdb_server.subtitles_list:
               subscounter = 0
               for item in self.osdb_server.subtitles_list:
                   listitem = xbmcgui.ListItem( label=item["language_name"], label2=item["filename"], iconImage=item["rating"], thumbnailImage=item["language_flag"] )
                   if item["sync"]:
                       listitem.setProperty( "sync", "true" )
                   else:
                       listitem.setProperty( "sync", "false" )
                   self.list.append(subscounter)
                   subscounter = subscounter + 1                                    
                   self.getControl( SUBTITLES_LIST ).addItem( listitem )

           self.getControl( STATUS_LABEL ).setLabel(( str( len ( self.osdb_server.subtitles_list ) )) + _( 744 ) + '"' + self.file_name + '"' )
           
           self.setFocus( self.getControl( SUBTITLES_LIST ) )
           self.getControl( SUBTITLES_LIST ).selectItem( 0 )
           
        except Exception, e:
            error = _( 634 ) % ( "search_subtitles:" + str ( e ) ) 
            LOG( LOG_ERROR, error )
            return False, error


###-------------------------- Podnapisi search   -------------################


    def search_subtitles_pod( self ):
        ok = False
        ok2 = False
        msg = ""
        
        self.getControl( STATUS_LABEL ).setLabel( _( 646 ) )    

        try:
            if not self.file_original_path.find("http") > -1 and not self.set_xbox :
                if self.debug : LOG( LOG_INFO, "Search by hash_pod [" +  os.path.basename( self.file_original_path ) + "]" )
                self.getControl( STATUS_LABEL ).setLabel( _( 642 ) % ( "...", ) )
                hashTry = timeout(self.set_filehash, timeout_duration=5)
                ok,msg = self.osdb_server.searchsubtitles_pod( self.search_string, hashTry ,self.lang_two1,self.lang_two2,self.lang_two3)
                if not ok:
                        self.connected = False
                if self.debug : LOG( LOG_INFO, "Hash Search_pod: [" + msg + "]" )
                        
            if (len ( self.osdb_server.subtitles_hash_list )) < 2:
                if self.debug : LOG( LOG_INFO,"Search by name_pod [" +  self.search_string + "]" )
                self.getControl( STATUS_LABEL ).setLabel( _( 642 ) % ( "......", ) )
                
                ok2,msg2 = self.osdb_server.searchsubtitlesbyname_pod( self.search_string, self.lang_two1,self.lang_two2,self.lang_two3, self.year )
                if self.debug : LOG( LOG_INFO, "Name Search_pod: [" + msg2 + "]" )
                
                
            self.osdb_server.mergesubtitles()
            if not ok and not ok2:
                self.getControl( STATUS_LABEL ).setLabel( _( 634 ) % ( msg, ) )
                
            label = ""
            self.list = []                    
            if self.OS :
                label2 = "[COLOR=FFFF0000]%s[/COLOR]" % (  _( 610 ) + "OpenSubtitles.org" )
                listitem = xbmcgui.ListItem( label,label2 )
                self.list.append("OS")                               
                self.getControl( SUBTITLES_LIST ).addItem( listitem )
            if self.mansearch :
                label2 = "[COLOR=FF00FF00]%s[/COLOR]" % (  _( 612 ) )
                listitem = xbmcgui.ListItem( label,label2 )
                self.list.append("MN")                                
                self.getControl( SUBTITLES_LIST ).addItem( listitem )
            if self.osdb_server.subtitles_list:                            
                subscounter = 0
                for item in self.osdb_server.subtitles_list:
                    listitem = xbmcgui.ListItem( label=item["language_name"], label2=item["filename"], iconImage=item["rating"], thumbnailImage=item["language_flag"] )
                    if item["sync"]:
                        listitem.setProperty( "sync", "true" )
                    else:
                        listitem.setProperty( "sync", "false" )
                    self.list.append(subscounter)
                    subscounter = subscounter + 1                                    
                    self.getControl( SUBTITLES_LIST ).addItem( listitem )

            self.getControl( STATUS_LABEL ).setLabel(   str( len ( self.osdb_server.subtitles_list ) ) + _( 744 ) + '"' + self.file_name + '"' )
            
            self.setFocus( self.getControl( SUBTITLES_LIST ) )
            self.getControl( SUBTITLES_LIST ).selectItem( 0 )
            
        except Exception, e:
            error = _( 634 ) % ( "search_subtitles:" + str ( e ) ) 
            LOG( LOG_ERROR, error )
            return False, error    

    
###-------------------------- Show control  -------------################
    
    
    def show_control( self, controlId ):
        self.getControl( STATUS_LABEL ).setVisible( controlId == STATUS_LABEL )
        self.getControl( SUBTITLES_LIST ).setVisible( controlId == SUBTITLES_LIST )
        page_control = ( controlId == STATUS_LABEL )
        try: self.setFocus( self.getControl( controlId + page_control ) )
        except: self.setFocus( self.getControl( controlId ) )


###-------------------------- Sub download OS and Podnapisi  -------------################


    def file_download(self, url, dest):
    
        if self.service == "Podnapisi":
           pod_url_parse = urllib.urlopen(url).read()
           url = "http://www.podnapisi.net/ppodnapisi/download/i/%s" % (pod_url_parse.split("/ppodnapisi/download/i/")[1].split('" title="')[0])
           print "Podnapisi Download URL: %s" % (url)      
        if self.debug : LOG( LOG_INFO, "Link download " + url )
        req = Request(url)
        f = urlopen(req)
        local_file = open(dest, "w" + "b")

        local_file.write(f.read())
        local_file.close()
            

    def download_subtitles(self, pos):
        if self.debug : LOG( LOG_INFO, "download_subtitles" )
        self.getControl( STATUS_LABEL ).setLabel(  _( 649 ) )
        if self.osdb_server.subtitles_list:
            filename = self.osdb_server.subtitles_list[pos]["filename"]
            url = self.osdb_server.subtitles_list[pos]["link"]
            local_path = __settings__.getSetting("subfolderpath")
            zip_filename = "special://temp/zipsubs.zip"
            sub_filename = os.path.basename( self.file_path )
            lang = toOpenSubtitles_two(self.osdb_server.subtitles_list[pos]["language_name"])
            subName1 = sub_filename[0:sub_filename.rfind(".")] 
            if subName1 == "":subName1 = self.search_string.replace("+", " ")
            self.file_download( url, zip_filename )
            self.extract_subtitles( filename, lang,subName1, zip_filename, local_path )


###-------------------------- Sub extract OS and Podnapisi  -------------################

             
    def extract_subtitles(self, filename, lang, subName1, zip_filename, local_path ):

        if self.debug : LOG( LOG_INFO, "extract_subtitles" )

        self.getControl( STATUS_LABEL ).setLabel(  _( 652 ) )
        # xbmc.Player().setSubtitles(xbmc.translatePath( os.path.join( os.getcwd(), 'resources', 'lib','dummy.srt' ) ) )
        
        try:
            un = unzip.unzip()
            files = un.get_file_list( zip_filename )
            if not zipfile.is_zipfile( zip_filename ) :
                self.getControl( STATUS_LABEL ).setLabel( _( 654 ) )
                subtitle_set = False
                label = ""
                self.list = []
                if self.PN :
                    label2 = "[COLOR=FFFF0000]%s[/COLOR]" % (  _( 610 ) + "Podnapisi.net" )
                    listitem = xbmcgui.ListItem( label,label2 )
                    self.list.append("PN")
                    self.getControl( SUBTITLES_LIST ).addItem( listitem )
                if self.mansearch :
                    label2 = "[COLOR=FF00FF00]%s[/COLOR]" % (  _( 612 ) )
                    listitem = xbmcgui.ListItem( label,label2 )
                    self.list.append("MN")
                    self.getControl( SUBTITLES_LIST ).addItem( listitem )
                        
            else:
                self.getControl( STATUS_LABEL ).setLabel( _( 650 ) )
                extracted_subtitles = un.extract( zip_filename, local_path )
                self.getControl( STATUS_LABEL ).setLabel( _( 651 ) )

                if self.debug : 
                    LOG( LOG_INFO, "Number of subs in zip:[%s]" ,str(len(extracted_subtitles)) )
                    LOG( LOG_INFO, "Files: [%s]", str(extracted_subtitles))
                    LOG( LOG_INFO, _( 644 ) % ( local_path ) )
                    LOG( LOG_INFO, _( 631 ) % ( zip_filename, local_path ) )

                print(os.path.join(local_path, extracted_subtitles[0]))
                xbmc.Player().setSubtitles(os.path.join(local_path, extracted_subtitles[0]))
            
                # movie_files     = []
                # number_of_discs = 1
                # sub_filename = os.path.basename( self.file_path )
            
                # movie_files.append(sub_filename)

                # self.getControl( STATUS_LABEL ).setLabel(  _( 652 ) )
                # zip = zipfile.ZipFile (zip_filename, "r")
                # i   = 0
                # for zip_entry in zip.namelist():
                #     if (zip_entry.find( "srt" ) < 0)  and (zip_entry.find( "sub" ) < 0)  and (zip_entry.find( "txt" )< 0) :
                #         os.remove( xbmc.translatePath("special://temp/" + zip_entry) )

                #     if ( zip_entry.find( "srt" )  > 0 ) or ( zip_entry.find( "sub" )  > 0 ) or ( zip_entry.find( "txt" )  > 0 ):
                    
                #         if i == 0 :
                #             i         = i + 1
                #             file_name = zip_entry
                #             sub_ext  = os.path.splitext( file_name )[1]
                #             sub_name = os.path.splitext( movie_files[i - 1] )[0]
                            
                #             file_name = "%s.%s%s" % ( sub_name, str(lang), ".srt" )
                #             file_path = os.path.join(self.sub_folder, file_name)

                #             try:
                #                     outfile   = open(file_path, "wb")
                #                     outfile.write( zip.read(zip_entry) )
                #                     outfile.close()
                #                     xbmc.Player().setSubtitles(file_path)
                #             except:
                #                     import xbmcgui
                #                     dialog = xbmcgui.Dialog()
                #                     selected = dialog.yesno("OpenSubtitles_OSD", "You can't save subtitle to Selected destination", "Please choose different Subtitle folder under Script Settings.", "Would you like to adjust the settings now?" )
                #                     if selected == 1:
                #                             __settings__.openSettings()                                                             
                             
                #             os.remove ( xbmc.translatePath("special://temp/" + zip_entry) )
                                                        
                # zip.close()

            os.remove(xbmc.translatePath(zip_filename))
            self.exit_script()            



        except Exception, e:
            error = _( 634 ) % ( str ( e ) )
            LOG( LOG_ERROR, error )
            
###-------------------------- Manual search Keyboard  -------------################


    def keyboard(self):
        sep = xbmc.translatePath(os.path.dirname(self.file_original_path))
        default = sep.split(os.sep)
        dir = default.pop()
        if str(dir) == "":
            default = sep.split("/")
            dir = default.pop()
        kb = xbmc.Keyboard(dir, 'Enter The Search String', False)
        text = self.search_string
        kb.doModal()
        if (kb.isConfirmed()): text = kb.getText()
        self.search_string = text.replace(" ","+")
        LOG( LOG_INFO, "Keyboard Entry: [%s]" ,  self.search_string )
        self.manuall = True
        self.connect()

###-------------------------- Exit script  -------------################

                
    def exit_script( self, restart=False ):
        self.close()

###-------------------------- Click  -------------################



    def onClick( self, controlId ):
        selected = self.list[self.getControl( SUBTITLES_LIST ).getSelectedPosition()]
        if self.debug : LOG( LOG_INFO, "In 'On click' selected : [%s]" , ( str(selected) ) )
        if selected == "OS":
            self.service = "OpenSubtitles"
            self.connect()
        elif selected == "PN":
            self.service = "Podnapisi"
            self.connect()
        elif selected == "MN":
            self.keyboard()
        else:
            if self.debug : LOG( LOG_INFO, "Selected :: [%s]" , ( str(selected) ) )                                
            if self.service == "OpenSubtitles":
                self.download_subtitles( selected )
            if self.service == "Podnapisi":
                self.download_subtitles( selected )                                                                                                             
        
###-------------------------- On Focus  -------------################
 
    
    def onFocus( self, controlId ):
        self.controlId = controlId

###-------------------------- "Esc" , "Back" button  -------------################
        
def onAction( self, action ):
    if ( action.getButtonCode() in CANCEL_DIALOG ):
        self.exit_script()


