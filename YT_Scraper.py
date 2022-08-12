import Utils
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import youtube_dl
import os

class Scraper:
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("headless")

        chromedriver_autoinstaller.install()
        
        self.driver = webdriver.Chrome(options=opt)
        self.search = r"https://www.youtube.com/results?search_query="
        
    def scrape_video(self, url): 
        if not "www.youtube.com" in url:
            self.scrape_video(self.get_search(url))
            return os.path.dirname(__file__) + "\\temp\\"
        
        ydl_opts = {
            "format": "22",
            "continue": True,
            "outtmpl": os.path.dirname(__file__) + "\\temp\\%(uploader)s - %(title)s.%(ext)s",
            "verbose": True,
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        return os.path.dirname(__file__) + "\\temp\\"
            
    def get_search(self, name):
        self.driver.get(self.search + name.replace(" ", "+"))
        self.driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        
        for result in self.driver.find_elements(By.CSS_SELECTOR, ".text-wrapper.style-scope.ytd-video-renderer"):
            return str(result.find_element(By.CSS_SELECTOR, ".title-and-badge.style-scope.ytd-video-renderer a").get_attribute("href"))
        
    def reset(self):
        tempdir = os.path.dirname(__file__) + "\\temp"
        
        for file in os.listdir(tempdir):
            f = tempdir + "\\" + file
            
            if os.path.isfile(f):
                os.remove(f)
                
        os.rmdir(tempdir)
