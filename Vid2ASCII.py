import VidConverter
import CLI_Player
import YT_Scraper
import sys

class Vid2ASCII:
    def __init__(self):
        self.yts = YT_Scraper.Scraper()
        self.vidc = VidConverter.Converter()
        self.cli = CLI_Player.Player()
    
    def play_url(self, url):
        vid = self.yts.scrape(url)
        #convert and play vid (maybe feed vidc into cli?)

def play(url):
    player = Vid2ASCII()
    player.play_url(url)

if __name__ == '__main__':
    play(sys.argv[1])