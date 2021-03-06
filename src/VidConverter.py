import PIL.Image as Image
import numpy as np
import cv2
import sys
import os

# ONLY FOR 1080P 1920 x 1080

cdir = os.path.split(__file__)[0] + "\\"

class Converter:
    density = list("""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'........___        """)
    
    def __init__(self):
        self.fps = 10
    
    def frame2ascii(self, frame):
        # loading & converting image to grayscale
        img = np.asarray(frame)
        assert img.shape == (1080, 1920, 3), "Media must be 1920x1080 (1080p)"
        
        greyscale_conv = np.array([0.2989, 0.587, 0.114])
        img = np.tensordot(img, greyscale_conv, axes=([2], [0]))
        
        # NOTE: loop step sizes are only configured for 1080p, change for different resolutions
        text = ""
        
        for y in range(0, img.shape[0], 25):
            for x in range(0, img.shape[1], 10):
                pix = img[y][x]
                text += self.density[round(((pix/255)) * len(self.density))]
            
            text += "\n"
        
        return text
    
    def breakdown(self, video):
        # arr of strings
        frames = []
        
        # breakdown + conversion of frames
        vidcap = cv2.VideoCapture(video)
        
        while True:
            success, frame = vidcap.read()
        
            if not success:
                break
            
            string_frame = self.frame2ascii(frame)     
            frames.append(string_frame)
            
        return frames

def main():
    c = Converter()
    ascii_vid = c.breakdown("samplevid.mp4")

if __name__ == '__main__':
    main()
    
