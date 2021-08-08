#Test Branch

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import pathlib
import time
from pandas import *

# URL-List

## URL-Dictionary mit Link-gemeinde-prefix value/keys
linklist = [
    'https://www.geo.lu.ch/map/grundbuchplan?FOCUS=2668836:1215000:12000',
    'https://www.geo.lu.ch/map/grundbuchplan?FOCUS=2665493:1214392:12000'
]

url_dir = {}
xls = ExcelFile(r'C:\Users\handb\Desktop\Screenshot\URLListe.xls')
df = xls.parse(xls.sheet_names[0])
url_dict = df.to_dict('records')


webdriverdir = r'C:\Users\handb\Desktop\Screenshot\chromedriver.exe'
dir = 'C:\\Users\\handb\\Desktop\\Screenshot\\images'

#Function

def URLSCREENER(linkdictionary, dir, webdriverdir):

    # WebDriver
            # webbrowser im hintergrund oeffnen ?!
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=webdriverdir)
    # driver.manage().timouts().implicitlyWait(5, TimeUnit.SECONDS)

    #Link and parameters from dictionary
            # fortschrittsbalken, links to creat etz.

    for e in linkdictionary:
        url= e.get("URL")
        gem= e.get("GEM")
        prefix= e.get("PREFIX")

        file= str(str(dir)+str("\\")+str(prefix)+str("_")+str(gem)+".png")

        driver.get(url)
        # driver.set_page_load_timeout(10)
        time.sleep(8)

        driver.save_screenshot(file)

        #crop
                #cropsize anpassen --> experience nachschauen wie gross printscreens eig. sind..
        element= driver.find_element_by_id("mapContainer");
        location = element.location
        size = element.size
        print(element,location,size)

        x = location['x'];
        y = location['y'];
        width = location['x'] + size['width'];
        height = location['y'] + size['height'];
        im = Image.open(file)
        im = im.crop((int(x), int(y), int(width), int(height)))
        cropfile = str(str(dir)+str("\\")+str(prefix)+str("_")+str(gem)+"_croped.png")
        im.save(cropfile)
    driver.close()
    print("finished")


URLSCREENER(url_dict,dir, webdriverdir)