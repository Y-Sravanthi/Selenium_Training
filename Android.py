import os

from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(_file_), p))


desired_caps = {'platformName': 'Android', 'platformVersion': '11.0', 'deviceName': 'Pixel 4',
                'app': PATH(r'D:\Downloads\Telegram.apk')}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)