from time import sleep

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import requests
#
# r = requests.get(
#     'http://tiqu.ipidea.io:2330/getProxyIp?num=100&return_type=txt&lb=1&sb=0&flow=1&regions=us&protocol=http')
# proxy = r.text.split('\r\n')[0]
proxy = 'http://104.208.139.238:80'
# proxy = 'socks5://' + proxy
print(proxy)
options = webdriver.ChromeOptions()
# 设置代理
options.add_argument('--proxy-server=%s' % proxy)
options.add_extension('Buste1.3.1.0.crx')

driver = webdriver.Chrome('chromedriver.exe', options=options)

driver.get("https://www.yalala.com/")
input("srt")
