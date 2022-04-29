#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import ip端口
import 鼠标控制
from 新建邮箱 import 邮箱注册
from 更换ip import 更换ip
from 鼠标控制 import 鼠标点击, 循环检测

re = "images/01.png"
继续 = "images/03.png"
人 = "images/04.png"
展开 = "images/05.png"
点击 = "images/06.png"
again = "images/08.png"
验证没有通过 = "images/11.png"
插件 = "images/14.png"
回话 = "images/15.png"
以游客 = "images/16.png"
关闭 = "images/17.png"
加 = "images/18.png"


def 输入邮箱账号(driver, 邮箱账号):
    driver.find_element(By.CSS_SELECTOR,
                        '#email').send_keys(
        邮箱账号)
    driver.find_element(By.CSS_SELECTOR,
                        '#reenter_email').send_keys(
        邮箱账号)


def 点击验证码():
    鼠标点击(点击)
    print("点击人")
    鼠标点击(re)
    print("点击re")
    sleep(2)
    鼠标点击(人)
    print("点击黄色人")
    sleep(2)
    if 循环检测(again, 1):
        return 1
    i = 0
    while i < 10:
        sleep(2)
        if 循环检测(继续, 1):
            鼠标点击(继续)
            print("点击继续")
            break
        else:
            鼠标点击(人)
            print("点击黄色人2")
            if 循环检测(again, 1):
                return 1
            i += 1
    if i == 10:
        return 1
    sleep(2)
    if 循环检测(验证没有通过, 1):
        return 1

    input('1')


def 新建窗口(driver):
    # 鼠标控制.鼠标点击(插件)
    # 鼠标控制.鼠标点击(回话)
    # 鼠标控制.鼠标点击(以游客)
    # 鼠标控制.鼠标点击(关闭)
    # drivers = driver.window_handles
    # driver.switch_to.window(drivers[-1])
    # driver.close()
    鼠标控制.鼠标点击(插件)
    鼠标控制.鼠标点击(回话)
    鼠标控制.鼠标点击(加)
    drivers = driver.window_handles
    driver.switch_to.window(drivers[-1])
    sleep(3)
    return driver


def 打开邮箱页面(邮箱账号):
    options = webdriver.ChromeOptions()
    # options.add_extension('Buste1.3.1.0.crx')
    # options.add_extension('360.crx')
    # proxy = ip端口.proxy
    # options.add_argument('--proxy-server=%s' % proxy)
    path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
    options.add_argument('--user-data-dir=' + path)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    # driver.maximize_window()
    driver.get("https://store.steampowered.com/join/")
    driver = 新建窗口(driver)

    driver.find_element(By.CSS_SELECTOR,
                        "#i_agree_check").click()

    输入邮箱账号(driver, 邮箱账号)
    是否验证成功 = 点击验证码()
    return 是否验证成功


if __name__ == "__main__":
    邮箱账号, 邮箱密码 = 邮箱注册()
    while True:
        # 更换ip()
        是否验证成功 = 打开邮箱页面(邮箱账号)
        if 是否验证成功 == 1:
            continue
        else:
            break
    # 打开邮箱页面()