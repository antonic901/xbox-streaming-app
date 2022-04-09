# Stream Movies & TV Shows
###### Stream Movies & TV Shows on your Original Xbox!

###### Hello to all! This is a project I have been working on for some time. Everything started with my motivation to learn how to make skins for Kodi, and because Kodi originated on Original Xbox (then called XBMC) I came to great idea to make program witch will stream Movies and TV Shows on this dated hardware. Motivation also came from desire to show why Xbox was a big deal back in the day and why it is such a great system. This console was ahead of it's time!

## Table of Contents
- [Info](#info)
- [Requirements](#requirements)
- [Setup Guide](#setup-guide)
- [Running](#running)
- [Functionalities](#functionalities)
  * [Xbox functionalities](#xbox)
  * [PC funcionalities](#pc)
- [Video](#video)
- [Some images](#some-images)
## Info
 - This project have two main applications. One is for PC coded in Node.js and other is program (script) for XBMC4Xbox coded in XML/Python. PC app is API which    serves requests from Xbox and it offeres torrent search engine, torrent stream and on-the-fly video convertion from H.264/265 to H.263 using ffmpeg. It also provides frontend coded in Vue.js which help you to easily organize and observe all torrents and to change some API config parameters like IP ADDRESS and PORT. Xbox app is a script for XBMC4Xbox where GUI is coded using XBMCGUI library and backend in python which communicate with TMDB and Trakt API.
 
 - GUI insipration is taken from XBMC Origins, Embuary Skin and Xbox Series S/X UI
 - Frontend GUI inspiration is taken from [VueTorrent](https://github.com/WDaan/VueTorrent)
  
## Requirements
- **Xbox**
    + You need softmodded or hardmodded Xbox
    + You need latest release of [XBMC4Xbox](https://www.dropbox.com/sh/8mcip8xsfe1zjap/AABSR3_toPPiFn-7OqwQY_JIa)
    + [OPTIONAL] 128MB RAM UPGRADE recommended, but not required
- **PC**
    + [Node.js](https://nodejs.org/en/download/)
    + [FFmpeg](https://www.ffmpeg.org/)
    + Modern PC with decent CPU and 4GB of RAM or more
    + PC with Windows, Linux or macOS

## Setup Guide
### Xbox
 - From this repo, copy addon-for-xbox/**Stream Movies & TV Shows** to scripts folder of XBMC4Xbox folder. In most cases it's: **E:\Apps\XBMC\scripts**
### PC
 - Install Node.js
 - Install FFmpeg

## Running
### Xbox
 - Open script from XBMC4Xbox located in Programs -> Scripts
### PC
 - Open backend-for-pc/xbox-classic-streamer in terminal/console and type:
      ```bash
      npm install
      node ./server/bin.js
      ```
 - Open frontend on http://YOUR_IP_ADDRESS:9005 in your browser
## Functionalities
Status values:
- ✓ - Functionality implemented
- ✗ - Functionality not yet implemented

## Xbox
| Functionality                                     | Status |
|---------------------------------------------------|:------:|
| Movies home page                                  |   ✓    |
| TV Shows home page                                |   ✓    |
| Search Movies                                     |   ✓    |
| Search TV Shows                                   |   ✓    |
| Info about Movie                                  |   ✓    |
| Info about TV Show                                |   ✓    |
| Info about actor                                  |   ✓    |
| Search subtitles                                  |   ✓    |
| Trakt implementation                              |   ✗    |

## PC
| Functionality                                     | Status |
|---------------------------------------------------|:------:|
| Find torrent streams                              |   ✓    |
| Get magnet link of torrent                        |   ✓    |
| Stream torrent                                    |   ✓    |
| Start torrent download                            |   ✓    |
| Stop torrent download                             |   ✓    |
| Get info about torrent                            |   ✓    |
| FFmpeg convertion to H.263                        |   ✓    |
| Frontend                                          |   ✓    |

## Support
<a href="https://www.buymeacoffee.com/antonic901" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Video
[![Watch the video](https://i.postimg.cc/MHwKGTNw/Screenshot-from-2022-03-24-23-32-49.png)](https://www.youtube.com/watch?v=IKsCAWdUhbw)
## Some images
![PC Dashboard](https://i.postimg.cc/cHLxYg8Z/Screenshot-from-2022-02-11-18-01-27.png)
![PC Settings](https://i.postimg.cc/50Kxm4wz/Screenshot-from-2022-02-11-18-01-49.png)
![Movies](https://i.postimg.cc/jScq6RNM/screenshot000.png)
![TV Shows](https://i.postimg.cc/ZYLTzTs4/screenshot001.png)
![Search movies](https://i.ibb.co/TTp5JL0/screenshot005.png)
![Movie info](https://i.postimg.cc/tJDy35nY/screenshot006.png)
![TV Search](https://i.ibb.co/y0w6dLn/screenshot003.png)
![TV Show info](https://i.postimg.cc/BQY4tmGz/screenshot004.png)
![Actor info](https://i.postimg.cc/BvD0Ys1W/screenshot007.png)
![Actor Info](https://i.postimg.cc/3xzhFWNC/screenshot008.png)
