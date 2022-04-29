#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

from 成功之后 import 退出Steam登录

def 读取账号密码():
    file = '成功注册的Steam账号.txt'
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
    账号信息 = random.choice(data).strip().split('----')
    print(账号信息)
    账号,密码 = 账号信息[2],账号信息[3]
    return 账号,密码


def 登录Steam(driver):
    driver.get("https://store.steampowered.com/login/")
    driver.switch_to.window(driver.current_window_handle)
    账号, 密码 = 读取账号密码()
    driver.find_element(By.CSS_SELECTOR, '#input_username').send_keys(账号)
    driver.find_element(By.CSS_SELECTOR, '#input_password').send_keys(密码)
    driver.find_element(By.CSS_SELECTOR, '#login_btn_signin > button').click()
    print('初始登录成功')
    退出Steam登录('初始', driver)


if __name__ == "__main__":
    账号,密码 = 读取账号密码()
    print(账号,密码)