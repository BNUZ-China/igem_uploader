from selenium.webdriver import Chrome
import os
import hashlib
import time
import pandas as pd
from FileManager import getFileList

class Uploader():
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.browser = Chrome()
        self.file_list = os.listdir(base_dir)
        self.names = []
        self.links = []

    def _setUploadFile(self, filepath):
        input_field = self.browser.find_element_by_name('wpUploadFile')
        input_field.send_keys(os.path.join(self.base_dir, filepath))

    def _setUploadName(self, uploadName):
        input_field = self.browser.find_element_by_name('wpDestFile')
        input_field.send_keys(f'T--BNUZ-China--{uploadName}')

    def _upload(self):
        input_field = self.browser.find_element_by_name('wpUpload')
        input_field.click()

    def calcFileMD5_8digit(self, filepath):
        file = open(os.path.join(self.base_dir, filepath), 'rb')
        content = file.read()
        md5 = hashlib.md5(content)
        file.close()
        return md5.hexdigest()[:8]

    def getLink(self):
        try:
            link = self.browser.find_elements_by_xpath('/html/body/div/div[3]/div[2]/div/div[1]/div[2]/a')[0]
            return link.get_attribute('href')
        except:
            input_field = self.browser.find_element_by_name('wpUploadIgnoreWarning')
            input_field.click()
            time.sleep(5)
            return self.getLink()


    def start(self):
        self.browser.get('https://2021.igem.org/Special:Upload')
        print('please log in. Type anything to continue.')
        # wait user login
        _ = input()
        print('start upload.')

        file_list = getFileList(self.base_dir)

        for file in file_list:
            self.browser.get('https://2021.igem.org/Special:Upload')
            self._setUploadFile(file['all_path'])
            self._setUploadName(file['file_md5_name'])
            self._upload()
            time.sleep(5)
            try:
                link = self.getLink()
            except:
                link = 'ERROR'
            self.names.append(file['all_path'])
            self.links.append(link)
            time.sleep(3)


    def closeAndOutput(self, name):
        df = pd.DataFrame([self.names, self.links], index=['names', 'links'])
        df.to_excel(f'{name}.xlsx')

if __name__ == '__main__':
    uploader = Uploader('D:/Code/iGem/Wiki/src/assets')
    uploader.start()
    uploader.closeAndOutput('all')



