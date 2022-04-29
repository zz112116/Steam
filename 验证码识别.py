#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

import func_timeout
from func_timeout import func_set_timeout
from selenium.webdriver.common.by import By


def 点击验证(driver):
    iframe_xpath = '/html/body/div[1]/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[5]/div/div[1]/div/div/div/iframe'
    while True:
        try:
            iframe = driver.find_element(By.XPATH, iframe_xpath)
            break
        except:
            pass
    driver.switch_to.frame(iframe)
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "html").click()
            print('点击验证')
            break
        except:
            pass
    driver.switch_to.default_content()



def 点击buster(driver):
    iframe_xpath2 = '/html/body/div[2]/div[4]/iframe'
    while True:
        try:
            iframe = driver.find_element(By.XPATH, iframe_xpath2)
            driver.switch_to.frame(iframe)
            break
        except:
            pass

    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "#rc-imageselect > div.rc-footer > div.rc-controls > div.primary-controls > div.rc-buttons > div.button-holder.help-button-holder").click()
            print('点击人')
            break
        except:
            pass
    driver.switch_to.default_content()

@func_set_timeout(5)
def 判断是否正确(driver):
    iframe_xpath2 = '/html/body/div[2]/div[4]/iframe'
    while True:
        try:
            iframe = driver.find_element(By.XPATH, iframe_xpath2)
            driver.switch_to.frame(iframe)
            break
        except:
            pass

    while True:
        try:
            a = driver.find_element(By.CSS_SELECTOR, "body > div > div > div:nth-child(1) > div.rc-doscaptcha-header > div").text
            print('a',a)
            if a == 'Try again later':
                print('Try again later')
                刷新验证码(driver)
                return a
        except:
            pass
    driver.switch_to.default_content()

@func_set_timeout(5)
def 刷新验证码(driver):
    driver.switch_to.default_content()
    iframe_xpath2 = '/html/body/div[2]/div[4]/iframe'

    while True:
        try:
            iframe = driver.find_element(By.XPATH, iframe_xpath2)
            driver.switch_to.frame(iframe)
            break
        except:
            pass

    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "#reset-button").click()
            print('点击刷新')
            break
        except:
            pass
    driver.switch_to.default_content()



def 点击验证码全(driver):
    while True:
        点击验证(driver)
        sleep(5)
        点击buster(driver)
        a = 判断是否正确(driver)
        if a != 'Try again later':
            break







if __name__ == "__main__":
    pass