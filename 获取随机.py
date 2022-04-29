#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

file = '随机8位.txt'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def 刷新(driver):
    # 刷新
    driver.find_element(By.CSS_SELECTOR,
                        "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > label.operation > button.refresh").click()

    suiji = driver.find_element(By.CSS_SELECTOR,
                                "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > label.pwd-show > input").get_attribute(
        'value')

    shouzimu = suiji[0]

    while is_number(shouzimu):
        driver.find_element(By.CSS_SELECTOR,
                            "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > label.operation > button.refresh").click()
        suiji = driver.find_element(By.CSS_SELECTOR,
                                    "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > label.pwd-show > input").get_attribute(
            'value')
        shouzimu = suiji[0]
    return suiji


def 获取随机8位():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.yalala.com/")
    driver.find_element(By.CSS_SELECTOR, "#app > section.bg-container > header > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > div > div.pwd-digits > button:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > div > div.pwd-check > label > input[type=checkbox]:nth-child(3)").click()
    for i in range(1000):
        a = 刷新(driver)
        a = a + "\n"
        with open('随机8位.txt', 'a') as f:
            f.write(a)


def 判断是否需要添加():
    sz = os.path.getsize(file)
    if sz == 0:
        print('文件位空执行1000次随机8位..')
        获取随机8位()


def 读取随机字符(c):
    for i in range(c):
        判断是否需要添加()
        with open(file, 'r') as fin:
            data = fin.read().splitlines(True)
        首行 = data[0].strip()
        with open(file, 'w') as fout:
            fout.writelines(data[1:])
        yield 首行
    print('成功获取'+str(c)+'个8位随机字符...')


if __name__ == "__main__":
    a = list(读取随机字符(2))
    print(a)
