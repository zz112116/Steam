#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from 获取随机 import 读取随机字符, 获取随机8位
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def 读取账号密码():
    l = list(读取随机字符(2))
    邮箱账号 = l[0]
    邮箱密码 = l[1]
    return 邮箱账号, 邮箱密码


def 邮箱后台注册(driver, 邮箱账号, 邮箱密码):
    driver.find_element(By.ID,
                        'zh').send_keys(
        邮箱账号)
    driver.find_element(By.ID,
                        'mima').send_keys(
        邮箱密码)
    driver.find_element(By.CSS_SELECTOR,
                        "#add").click()
    driver.find_element(By.CSS_SELECTOR,
                        "body > div:nth-child(6) > a").click()


def 邮箱后台登录和注册(邮箱账号, 邮箱密码):
    # 邮箱后台登录
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://124.156.0.101:88/")
    driver.find_element(By.CSS_SELECTOR,
                        '#maintable > tbody > tr > td > form > table > tbody > tr > td > input[type=text]:nth-child(4)').send_keys(
        "Administrator")
    driver.find_element(By.CSS_SELECTOR,
                        '#maintable > tbody > tr > td > form > table > tbody > tr > td > input[type=password]:nth-child(8)').send_keys(
        "zz112116")
    driver.find_element(By.CSS_SELECTOR,
                        "#maintable > tbody > tr > td > form > table > tbody > tr > td > input[type=submit]:nth-child(11)").click()
    driver.get("http://124.156.0.101:88/account.php")
    print('邮箱后台登录成功.')
    邮箱后台注册(driver, 邮箱账号, 邮箱密码)


def 邮箱注册():
    邮箱账号, 邮箱密码 = 读取账号密码()
    邮箱后台登录和注册(邮箱账号, 邮箱密码)
    邮箱账号 = 邮箱账号 + '@wleizz.com'
    print(邮箱账号, 邮箱密码, "注册成功")
    return 邮箱账号, 邮箱密码


def 判断是否需要添加():
    file = '随机8位.txt'
    sz = os.path.getsize(file)
    if sz == 0:
        print('文件位空执行1000次随机8位..')
        获取随机8位()


def 读取随机字符(c):
    file = '随机8位.txt'
    for i in range(c):
        判断是否需要添加()
        with open(file, 'r') as fin:
            data = fin.read().splitlines(True)
        首行 = data[0].strip()
        with open(file, 'w') as fout:
            fout.writelines(data[1:])
        yield 首行
    print('成功获取' + str(c) + '个8位随机字符...')




def 邮箱提取():
    file = '邮箱批量注册结果2.txt'
    sz = os.path.getsize(file)
    if sz == 0:
        print('邮箱提取为空，执行邮箱注册..')
        邮箱账号, 邮箱密码 = 邮箱注册()
        return 邮箱账号, 邮箱密码
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
    首行 = data[0].strip()
    with open(file, 'w') as fout:
        fout.writelines(data[1:])
    l = 首行.split('----')
    # print(l)
    邮箱账号, 邮箱密码 = l[0],l[1]
    print('获取邮箱成功...')
    print(邮箱账号, 邮箱密码)
    return 邮箱账号, 邮箱密码

if __name__ == "__main__":
    # 邮箱账号, 邮箱密码 = 邮箱注册()
    # 邮箱账号, 邮箱密码 = 邮箱提取()
    # a = 邮箱账号.strip()
    # print(a)
    邮箱提取()