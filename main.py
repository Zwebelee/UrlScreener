#Test Branch


from selenium import webdriver
from PIL import Image
import pathlib
linklist = ['https://www.geo.lu.ch/map/grundbuchplan?FOCUS=2668836:1215000:12000','https://www.geo.lu.ch/map/grundbuchplan?FOCUS=2648836:1235000:12000']

url = linklist[0]
url = "https://www.google.com"

driver = webdriver.Chrome()
driver.get(url)
driver.save_screenshot("image.png")

driver.save_screenshot("C:\TestTemp\image.png")
dir = "C:\TestTemp\image2.png"
driver.save_screenshot(dir)
pathdir = pathlib.Path(dir)
driver.save_screenshot(pathdir)

image = Image.open("image.png")
image.show

i=0
def SC(url, dir, prefix,i):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\Andi SamLap\Downloads\chromedriver_win32\chromedriver.exe')

    driver.get(url)
    driver.set_page_load_timeout(10)

    filedir = dir
    filename = prefix+str(i)+'.png'
    filecomb = dir+filename
    print(filedir,filename,filecomb)

    driver.save_screenshot(filecomb)
    #image = Image.open("image.png")
    #image.show()
    driver.close()

testdir_o ='C:\TestTemp'
testdir = pathlib.Path(testdir_o)
testprefix = "\\test"

filedir = testdir
filename = testprefix+str(0)+'.png'
ff = filedir.joinpath(filename)

i=0
for link in linklist:
    SC(link,testdir_o,testprefix,i)
    print(link,testdir,testprefix)
    i+=1