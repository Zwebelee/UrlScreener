#Test Branch

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import pathlib
import time
from pandas import *

# URL-List

## URL-Dictionary mit Link-gemeinde-prefix value/keys
url_dict = {}
xlsx = ExcelFile(r'C:\Users\handb\Desktop\URL\URL_LIST.xlsx')
df = xlsx.parse(xlsx.sheet_names[0])
url_dict = df.to_dict('records')


webdriverdir = r'C:\Users\handb\Desktop\Screenshot\chromedriver.exe'
dir = 'C:\\Users\\handb\\Desktop\\Screenshot\\images'

#Function

def URLSCREENER(linkdictionary, dir, webdriverdir):

    # Get list infos
    i = 0
    for e in linkdictionary:
        i+=1
    print("Links to process: {}".format(i))
    list_count = i

    # WebDriver
            # webbrowser im hintergrund oeffnen ?!
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=webdriverdir)
    # driver.manage().timouts().implicitlyWait(5, TimeUnit.SECONDS)

    #Link and parameters from dictionary
    i=0
    for e in linkdictionary[:2]:
        url= e.get("URL")
        gem= e.get("Gemeinde")
        prefix= e.get("Produkt")
        gem_kuerzel = e.get("Kürzel")

        file= str(str(dir)+str("\\")+str(prefix)+str("_")+str(gem_kuerzel)+".png")

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
        cropfile = str(str(dir)+str("\\")+str(prefix)+str("_")+str(gem_kuerzel)+"_croped.png")
        im.save(cropfile)
        i+=1
        sys.stdout.write("\rProcessed: %i of %i" % (i,list_count))
        driver.close()
    sys.stdout.flush()
    print("Finished")


URLSCREENER(url_dict,dir, webdriverdir)

i=0
for i in range(100):
    i+=1
    sys.stdout.write("\rProcess: %i" %i)
    sys.stdout.flush()