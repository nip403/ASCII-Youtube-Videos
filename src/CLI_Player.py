#play video in cli
#ideally match frame rate + play audio
# need to print screen then clear in cmd line
import sys
import os
import time

class Player:
    def __init__(self):
        pass
    
    def play(self, frames):
        for i in frames:
            os.system("cls")
            sys.stdout.write(i)
            time.sleep(1/30)
            
