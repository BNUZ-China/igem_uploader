from html_uploader import runOnSingleFolderHTML
from code_core import runOnSingleFolder
from code_uploader import Uploader
import time

location = '../Wiki/production'
browser = Uploader(isClear=False)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

runOnSingleFolder(location, 'js', browser)
runOnSingleFolder(location, 'css', browser)

browser.setClear(True)

runOnSingleFolderHTML(location, '.', browser)
# 15602310930
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
