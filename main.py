#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from time import sleep

from selenium import webdriver

from adspower接口调用 import 判断账号是否打开, 关闭某账号浏览器, 打开某账号浏览器, 创建账号, 删除账号
from steam邮箱页面a import 邮箱页面操作
from 成功之后 import 成功之后
from 新建邮箱 import 邮箱注册, 邮箱提取
from 登录Steam import 登录Steam


if __name__ == "__main__":
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    i = input('1:创建账号2：不创建')
    if i == '1':
        账号 = 创建账号()
    else:
        账号 = i
    if 判断账号是否打开(账号):
        关闭某账号浏览器(账号)
        sleep(3)

    while True:
        try:
            driver = 打开某账号浏览器(账号)
            登录Steam(driver)
            break
        except:
            关闭某账号浏览器(账号)
            sleep(3)

    判断次数 = 0
    成功次数 = 0
    while 判断次数 < 2:

        邮箱账号, 邮箱密码 = 邮箱提取()
        print('判断错误'+str(判断次数)+'次')
        是否成功, Steam注册页面句柄 = 邮箱页面操作(driver, 邮箱账号)
        # if 是否成功 == 3:
        #     关闭某账号浏览器(账号)
        #     sleep(3)
        #     driver = 打开某账号浏览器(账号)
        #     是否成功, Steam注册页面句柄 = 邮箱页面操作(driver, 邮箱账号)
        if 是否成功 == '成功':
            判断次数 = 0
            成功次数 += 1
            print('成功次数'+str(成功次数))
            print(是否成功)
            成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        elif 是否成功 == '次数到了':
            print(是否成功)
            关闭某账号浏览器(账号)
            sleep(3)
            删除账号(账号)
            break

        else:
            print(是否成功)
            判断次数 += 1
            continue
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('成功次数' + str(成功次数))
    关闭某账号浏览器(账号)
    sleep(3)

        # elif 是否成功 == '没点我同意':
        #     print('次数到了')
        #     是否成功, Steam注册页面句柄 = 没点击我同意(driver)
        #     if 是否成功 == 1:
        #         成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        #     else:
        #         print('验证失败，重新验证')
        #         是否成功, Steam注册页面句柄 = 邮箱操作失败(driver, Steam注册页面句柄)
        #         if 是否成功 == 1:
        #             成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        #         else:
        #             print('验证失败，重新验证')
        #             是否成功, Steam注册页面句柄 = 邮箱操作失败(driver, Steam注册页面句柄)
        #             if 是否成功 == 1:
        #                 成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        #             else:
        #
        #                 关闭某账号浏览器(账号)
        #                 sleep(3)
        #                 break
        # elif 是否成功 == '没填邮箱':
        #     print('没填邮箱')
        #     driver.refresh()
        #     是否成功, Steam注册页面句柄 = 邮箱页面操作(driver, 邮箱账号)
        #     if 是否成功 == 1:
        #         成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        #     else:
        #         print('验证失败，重新验证')
        #         是否成功, Steam注册页面句柄 = 邮箱操作失败(driver, Steam注册页面句柄)
        #         if 是否成功 == 1:
        #             成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        #
        #         else:
        #             print('验证失败，重新验证')
        #             是否成功, Steam注册页面句柄 = 邮箱操作失败(driver, Steam注册页面句柄)
        #             if 是否成功 == 1:
        #                 成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        #             else:
        #
        #                 关闭某账号浏览器(账号)
        #                 sleep(3)
        #                 break
        #
        # elif 是否成功 == '等待验证码超时':
        #     print('等待验证码超时')
        #     关闭某账号浏览器(账号)
        #     sleep(3)
        #     # 删除账号(账号)
        #     break
        # else:
        #
        #     print('验证失败，重新验证')
        #     是否成功, Steam注册页面句柄 = 邮箱操作失败(driver, Steam注册页面句柄)
        #     if 是否成功 == 1:
        #         成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        #     else:
        #         print('验证失败，重新验证')
        #         是否成功, Steam注册页面句柄 = 邮箱操作失败(driver, Steam注册页面句柄)
        #         if 是否成功 == 1:
        #             成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
        #         else:
        #
        #
        #             关闭某账号浏览器(账号)
        #             sleep(3)
        #             break







            # print('验证失败，重新验证')
            # 关闭某账号浏览器(账号)
            # break






            # print('验证失败，重新验证')
            # 是否成功, Steam注册页面句柄 = 邮箱操作失败(driver, Steam注册页面句柄)
            # if 是否成功:
            #     成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
            # else:
            #     print('验证失败，重新验证')
            #     是否成功, Steam注册页面句柄 = 邮箱操作失败(driver, Steam注册页面句柄)
            #     if 是否成功:
            #         成功之后(driver, 邮箱账号, 邮箱密码, Steam注册页面句柄)
            #     else:
            #         关闭某账号浏览器(账号)
            #         sleep(3)
            #         # 删除账号(账号)
            #         break