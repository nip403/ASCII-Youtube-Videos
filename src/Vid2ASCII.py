import VidConverter
import CLI_Player
import YT_Scraper
import sys
import os


class Vid2ASCII:
    def __init__(self):
        self.yts = YT_Scraper.Scraper()
        self.vidc = VidConverter.Converter()
        self.cli = CLI_Player.Player()
    
    def play_url(self, url):
        vid = self.yts.scrape(url)
        #convert and play vid (maybe feed vidc into cli?)
        
    def play_vid(self, fp):
        ascii_vid = self.vidc.breakdown(fp)
        self.cli.play(ascii_vid)

def play(url):
    player = Vid2ASCII()
    player.play_url(url)

if __name__ == '__main__':
    #play(sys.argv[1])
    cdir = os.path.split(__file__)[0] + "\\"
    b = Vid2ASCII()
    b.play_vid(cdir + "samplevid.mp4")
