import VidConverter
import YT_Scraper
import Utils
import logging
import sys
import os

logger = logging.getLogger("Utils.Vid2ASCII")

class Vid2ASCII:
    def __init__(self):
        self.yts = YT_Scraper.Scraper()
        self.vidc = VidConverter.Converter()
        
    def play_vid(self, args):
        if args.file is not None:
            self.vidc.load(args.file, args.playback)
            
        elif args.video is not None:
            tempdir = self.yts.scrape_video(args.video)
            
            file = sorted([os.path.join(tempdir, i) for i in os.listdir(tempdir)], key=os.path.getmtime)[-1]
            self.vidc.load(file, args.playback)
            
            self.yts.reset()

if __name__ == '__main__':
    args = Utils.parser.parse_args()
    Utils.validate_args(args)
    player = Vid2ASCII()
    player.play_vid(args)
