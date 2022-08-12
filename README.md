# ASCII-Youtube-Videos
Command line tool which converts videos into ASCII.

# Usage
```
usage: Vid2ASCII.py [-h] [--yt VIDEO] [--fp filepath] [--fullplayback bool] [--delete bool]

optional arguments:
  -h, --help            show this help message and exit

Video selection:
  --yt VIDEO, --url VIDEO
                        YT URL or video name, will select the top video from search results if not using URL
  --fp filepath, --file filepath
                        Full filepath to video

Other options:
  --fullplayback bool, -f bool
                        Playback mode:
                              (DEFAULT) 0: Play ASCII video as each frame loads (variable fps)
                                        1: Play ASCII video once whole video is processed (slower but reliable fps)
  --delete bool, -d bool
                        Delete downloaded video after playback (only for provided --yt/--url):
                                        0: Keep in temp directory
                              (DEFAULT) 1: Delete

Valid file types: .mp4
```

# Dependencies
- numpy
- cv2
- pillow
- selenium
- youtube-dl
- chromedriver_autoinstaller
