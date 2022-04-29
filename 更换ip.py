from time import sleep
import json
import urllib.request

from selenium import webdriver
import 鼠标控制
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

移动到24000 = "images/09.png"
ip刷新 = "images/10.png"
点击911图标 = "images/12.png"
刷新911 = "images/13.png"


def 更换ip():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:22999")
    鼠标控制.鼠标移动(移动到24000)
    鼠标控制.鼠标点击(ip刷新)
    sleep(3)
    print('ip跟换成功..')


def 跟换ip911():
    鼠标控制.鼠标点击(点击911图标)
    sleep(1)
    鼠标控制.鼠标点击(刷新911)
    # 鼠标控制.鼠标双击(100, 410)


def ip获取():
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {
                'http': 'http://lum-customer-hl_6dec02b3-zone-steam-country-us:gnx7utn6fat8@zproxy.lum-superproxy.io:22225',
                'https': 'http://lum-customer-hl_6dec02b3-zone-steam-country-us:gnx7utn6fat8@zproxy.lum-superproxy.io:22225'}))
    ip = json.loads(opener.open('http://lumtest.com/myip.json').read().decode('UTF-8'))['ip']
    print('获取到的ip为：' + ip)
    return ip


if __name__ == "__main__":
    # 更换ip()
    ip获取()
