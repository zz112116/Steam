#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import requests

from ip端口 import port


def 打开某账号浏览器(ads_id):
    ads_id = ads_id
    open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id

    resp = requests.get(open_url).json()
    if resp["code"] != 0:
        print(resp["msg"])
        print("please check ads_id")
        sys.exit()

    chrome_driver = resp["data"]["webdriver"]
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    print(ads_id + '打开成功')

    return driver


def 关闭某账号浏览器(ads_id):
    close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id
    # driver.quit()
    requests.get(close_url)


def 创建账号():
    url = 'http://local.adspower.net:50325/api/v1/user/create'
    headers = {'Content-Type': 'application/json'}
    data = {
        'domain_name': 'https://store.steampowered.com/join/',
        'open_urls': ['https://store.steampowered.com/join/'],
        'group_id': '0',
        # 'user_proxy_config':{"proxy_soft": "other", "proxy_type": "http", "proxy_host": "server.iphtml.biz", "proxy_port": "15000", "proxy_user": "uid-10604-zone-Steamqaqw",
        #  "proxy_password": "t37t9zw1"},
        #  'user_proxy_config':{"proxy_soft": "other", "proxy_type": "socks5", "proxy_host": "gate14.rola.info", "proxy_port": "2034", "proxy_user": "q112116_1", "proxy_password": "321478"},
        # 'user_proxy_config': {"proxy_soft": "other", "proxy_type": "socks5", "proxy_host": "127.0.0.1", "proxy_port": port},
        'user_proxy_config': {"proxy_soft": "911"},
        'fingerprint_config': {"canvas": "1", "webgl_image": "1", "language_switch": "1", "webgl": "1", "audio": "1",
                               "scan_port_type": "1",
                               "media_devices": "1", "device_name_switch": "1", "speech_switch": "1",
                               "mac_address_config": {"model": "1"}},
        'country': 'US'
    }
    x = requests.post(url=url, headers=headers, data=json.dumps(data)).json()
    # print(x)
    账号 = x['data']['id']
    print('账号:' + 账号 + ' 创建成功')
    return 账号


def 删除账号(账号):
    url = 'http://local.adspower.net:50325/api/v1/user/delete'
    headers = {'Content-Type': 'application/json'}
    data = {
        'user_ids': [账号]
    }
    x = requests.post(url=url, headers=headers, data=json.dumps(data)).json()
    if x['code'] == 0:
        print('账号：' + 账号 + ' 删除成功')
    else:
        print(账号 + '删除失败：' + x['msg'])


def 判断账号是否打开(ads_id):
    url = "http://local.adspower.net:50325/api/v1/browser/active?user_id=" + ads_id
    resp = requests.get(url).json()
    # print(resp)
    if resp['code'] == 0 and resp['data']['status'] == 'Active':
        print(ads_id, '已经打开')
        return True
    else:
        return False


if __name__ == "__main__":
    # ip = ip获取()
    账号 = 创建账号()

    打开某账号浏览器(账号)
    # 删除账号(账号)
    # 判断账号是否打开('j21kjoh')
    # 关闭某账号浏览器('j21kjoh')
