from typing import KeysView
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import os
import hashlib
import time
import pandas as pd
import pyperclip
from sip import ispycreated

class Uploader():
    def __init__(self, isClear):
        # options = ChromeOptions()
        # options.add_argument('-enable-webgl --no-sandbox --disable-dev-shm-usage')
        self.browser = Chrome()
        self.isClear = isClear
        self.browser.get('https://2021.igem.org/Team:BNUZ-China')
        print('wait login')
        _ = input()

    
    def upload(self, url, code):
        self.browser.get(url)
        pyperclip.copy(code)
        # time.sleep(3)

        while True:
            try:
                code_box = self.browser.find_element_by_name('wpTextbox1')
                break
            except:
                self.browser.refresh()
        if self.isClear:
            if code_box.text != "":
                code_box.clear()
            code_box.send_keys(Keys.CONTROL, 'V')    
            
        else:
            if code_box.text == "":
                code_box.send_keys(Keys.CONTROL, 'V')    
                   
        # time.sleep(3)

        upload_btn = self.browser.find_element_by_name('wpSave')
        upload_btn.click()

    def setClear(self, isClear):
        self.isClear = isClear

