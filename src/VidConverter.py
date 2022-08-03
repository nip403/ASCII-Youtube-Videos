import Utils
import PIL.Image as Image
import numpy as np
import cv2
import logging
import time
import sys
import os

#TODO NOTE in future when implementing audio playback may need to add cli player class back

cdir = os.path.split(__file__)[0] + "\\"
logger = logging.getLogger("Utils.Vid2ASCII.VidConverter")

#density = [' ', ' ', '_', '_', '.', ',', '`', '`', '-', ':', ';', '+', '*', '?', '%', 'S', 'W', 'M', '#', '@', '$'][::-1]
#density = list("""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'........___        """)
#density = list("""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'........___        """)
#density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\'.            "

def play(frame, fps, actualfps):
    sys.stdout.write(f"{frame}\nFPS: {actualfps}\nEXPECTED: {fps}\r")

def playall(frames, fps):
    for f in frames:
        t = time.time()
        time.sleep(1/fps)
        play(f, fps, 1/(time.time() - t))
        
class Converter:
    def __init__(self):
        self.density = [' ', ' ', '_', '_', '.', ',', '`', '`', '-', ':', ';', '+', '*', '?', '%', 'S', 'W', 'M', '#', '@', '$'][::-1] #TODO fix this with original once contrast stuff is done
        
    def load(self, filepath, playback):
        video = cv2.VideoCapture(filepath)
        
        if playback:
            self.full_breakdown(video)
        else:
            self.realtime_breakdown(video)
        
    def full_breakdown(self, video):
        fps = video.get(cv2.CAP_PROP_FPS)
        frames = []
        
        while True:
            t = time.time()
            success, frame = video.read()
        
            if not success:
                break
            
            frames.append(self.frame2ascii(frame))  
            
        playall(frames, fps)
            
    def realtime_breakdown(self, video):
        fps = video.get(cv2.CAP_PROP_FPS)
        
        while True:
            t = time.time()
            success, frame = video.read()
        
            if not success:
                break
            
            play(self.frame2ascii(frame), fps, 1/(time.time() - t))
    
    def frame2ascii(self, frame):
        """
        IMAGE PREPROCESSING
        """
        
        ##TODO next up implement contrast
        
        img = np.asarray(frame)
        
        # change resolution, numbers based on tested values for 1080p video
        xStep = int(10 * (img.shape[1]/1920))
        yStep = int(20 * (img.shape[0]/1080))
        
        x_neighbour = xStep // 2 + 1
        y_neighbour = yStep // 2 + 1
        
        # grayscale conversion
        greyscale_img = np.tensordot(img, [0.2989, 0.587, 0.114], axes=([2], [0]))
        text = ""
        
        #colourmap = np.zeros((greyscale_img.shape[0] // yStep + 1, greyscale_img.shape[1] // xStep + 1, 3))
        
        for y in range(0, greyscale_img.shape[0], yStep): 
            for x in range(0, greyscale_img.shape[1], xStep):
                
                # greyscale conversion
                pix = greyscale_img[y, x]
                text += self.density[np.floor(pix / 256 * len(self.density)).astype(int)]
                
                # colour average
                """ COLOUR IMPLEMENTATION BELOW, ON HOLD UNTIL I CAN BOTHER TO FIND A MORE EFFICIENT METHOD (IS MAD SLOW SEND HALP)
                xLow = x - x_neighbour if not x - x_neighbour < 0 else 0
                yLow = y - y_neighbour if not y - y_neighbour < 0 else 0
                
                xHigh = x + x_neighbour if not x + x_neighbour > greyscale_img.shape[1] - 1 else greyscale_img.shape[1] - 1
                yHigh = y + y_neighbour if not y + y_neighbour > greyscale_img.shape[0] - 1 else greyscale_img.shape[0] - 1
                
                slice_colour = img[yLow:yHigh, xLow:xHigh, :]
                flattened = np.reshape(slice_colour, (slice_colour.shape[0] * slice_colour.shape[1], 3))
                mean_colour = np.mean(flattened, axis=0)
                colourmap[y // yStep, x // xStep] = mean_colour
                """
                
            text += "\n"
        
        # TODO test yield with generator
        return text # return text, colourmap
