import os
from subprocess import run
import pyperclip
import webbrowser
from urllib import parse
from code_uploader import Uploader
import time

def runOnSingleFolderHTML(location, folder, browser):
    file_list = os.listdir(os.path.join(location, folder))

    for file in file_list:
        if file[-4:] == 'html':
            file_noextend = file[:-5]
            url = f'https://2021.igem.org/wiki/index.php?title=Team:BNUZ-China/{file_noextend}&action=edit'
            # url = f'https://2021.igem.org/wiki/index.php?title=Template:BNUZ-China/{folder}/{parse.quote(file_noextend)}&action=edit'
            with open(os.path.join(location, folder, file), encoding='utf-8') as f:
                content = f.read()
                browser.upload(url, content[15:])
