#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from func_timeout import func_set_timeout
import func_timeout
from selenium.webdriver.common.by import By

from 获取随机 import 读取随机字符


def 邮箱登录(driver, 邮箱账号, 邮箱密码):
    while True:
        try:
            js = 'window.open("http://mail.wleizz.com/");'
            driver.execute_script(js)
            drivers = driver.window_handles
            driver.switch_to.window(drivers[-1])
            driver.find_element(By.CSS_SELECTOR, '#rcmloginuser').send_keys(邮箱账号)
            break
        except:
            pass
    driver.find_element(By.CSS_SELECTOR, '#rcmloginpwd').send_keys(邮箱密码)
    driver.find_element(By.CSS_SELECTOR, "#rcmloginsubmit").click()


@func_set_timeout(30)
def 循环等待邮箱列表(driver):
    while True:
        try:
            driver.find_element(By.XPATH, '//*[@id="rcmbtn107"]').click()
            sleep(3)
        except:
            pass
        元素 = driver.find_elements(By.XPATH, '//*[@id="messagelist"]/tbody/tr')
        if 元素 != []:
            元素[0].click()
            break


@func_set_timeout(10)
def 点击Steam链接(driver):
    iframe_xpath = '#messagecontframe'
    Steam链接_xpath = '//*[@id="message-htmlpart1"]/div/center[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a'
    while True:
        try:
            iframe = driver.find_element(By.CSS_SELECTOR, iframe_xpath)
            driver.switch_to.frame(iframe)
            break
        except:
            pass
    while True:
        try:
            driver.find_element(By.XPATH, Steam链接_xpath).click()
            driver.switch_to.default_content()
            print('点击Steam链接成功')
            break
        except:
            pass


def 邮箱登录点击邮件(driver):
    while True:
        while True:
            try:
                循环等待邮箱列表(driver)
                break
            except func_timeout.exceptions.FunctionTimedOut:
                print('邮箱列表等待超时')
                driver.refresh()
        try:
            点击Steam链接(driver)
            break
        except func_timeout.exceptions.FunctionTimedOut:
            print('点击Steam链接失败')
            driver.refresh()


def 退出邮箱登录(driver):
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, '#rcmbtn105').click()
            driver.close()
            break
        except:
            pass


def 判断是否成功并且关闭页面(driver):
    drivers = driver.window_handles
    driver.switch_to.window(drivers[-1])
    text = driver.find_element(By.CSS_SELECTOR, '#main_content > div.newaccount_email_verified_text').text
    if text == 'Please return to the account creation window to complete creating your new Steam account.':
        print('返回注册页面成功')
        driver.close()
    else:
        print('返回注册页面失败')


def 选择窗口(driver, Steam注册页面句柄):
    driver.switch_to.window(Steam注册页面句柄)


def 判断错误是否存在(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, '#error_display')
        return True
    except:
        return False


@func_set_timeout(8)
def 等待点击(driver, Steam账号):
    while True:
        try:
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '#createAccountButton').click()
            print(Steam账号, '注册成功')
            sleep(1)
        except:
            break


def 创建用户(driver):
    a = list(读取随机字符(2))
    Steam账号 = a[0]
    Steam密码 = a[1]
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, '#accountname').send_keys(Steam账号)
            break
        except:
            pass
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(Steam密码)
    driver.find_element(By.CSS_SELECTOR, '#reenter_password').send_keys(Steam密码)
    try:
        等待点击(driver, Steam账号)
    except func_timeout.exceptions.FunctionTimedOut:
        pass
    return Steam账号, Steam密码

def 退出Steam登录(邮箱账号, driver):
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "#account_pulldown").click()

            break
        except:
            pass
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "#account_dropdown > div > a:nth-child(3)").click()

            break
        except:
            pass
    print(邮箱账号, 'Steam账号成功退出')


def 写入注册成功(邮箱账号, 邮箱密码, Steam账号, Steam密码):
    file = '成功注册的Steam账号.txt'
    data = 邮箱账号 + '----' + 邮箱密码 + '----'+Steam账号+'----'+Steam密码+'\n'
    with open(file, 'a') as fout:
        fout.write(data)
    print('账号写入成功')


def 成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄):
    邮箱登录(driver, 邮箱账号, 邮箱密码)
    邮箱登录点击邮件(driver)
    退出邮箱登录(driver)
    判断是否成功并且关闭页面(driver)
    选择窗口(driver, Steam注册页面句柄)
    Steam账号, Steam密码 = 创建用户(driver)
    print(邮箱账号, 邮箱密码, Steam账号, Steam密码)
    退出Steam登录(邮箱账号, driver)
    写入注册成功(邮箱账号, 邮箱密码, Steam账号, Steam密码)
    # 退出登录之后(driver)


if __name__ == "__main__":
    # 成功之后()
    # 写入注册成功('1', '1', '1', '1')
    pass
