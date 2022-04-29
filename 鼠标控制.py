#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import pyautogui


# import timeout_decorator
#
#
# @timeout_decorator.timeout(10)
def 鼠标点击(img):
    while True:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            break
        sleep(0.1)


def 鼠标双击(x, y):
    pyautogui.click(x, y, clicks=2, interval=0.2, duration=0.2, button="left")
    sleep(0.1)


def 鼠标移动(img):
    while True:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.moveTo(location)
            break
        sleep(0.1)


def 循环检测(img, time):
    i = 0
    sleep(2)
    while i < time:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            return True
        sleep(1)
        i += 1
    return False


if __name__ == "__main__":
    pass
