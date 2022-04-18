from time import sleep
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

# import requests
#
# r = requests.get('http://tiqu.ipidea.io:2330/getProxyIp?num=100&return_type=txt&lb=1&sb=0&flow=1&regions=us&protocol=http')
# proxy = r.text.split('\r\n')[0]
options = webdriver.ChromeOptions()
# 设置代理

options.add_extension('Buste1.3.1.0.crx')
proxy = ['socks5://192.168.31.225:5000']
proxy = random.choice(proxy)
print(proxy)
options.add_argument('--proxy-server=%s' % proxy)
driver = webdriver.Chrome('chromedriver.exe', options=options)

driver.maximize_window()
driver.get('chrome://settings/clearBrowserData')
driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)


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


def 关闭网页():
    driver.quit()


def 关闭当前窗口():
    driver.close()


def 邮箱后台登录():
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


def 邮箱注册(邮箱账号, 邮箱密码):
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


def 获取随机8位():
    driver.get("https://www.yalala.com/")
    driver.find_element(By.CSS_SELECTOR, "#app > section.bg-container > header > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > div > div.pwd-digits > button:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > div > div.pwd-check > label > input[type=checkbox]:nth-child(3)").click()
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

    driver.find_element(By.CSS_SELECTOR,
                        "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > label.operation > button.refresh").click()
    suiji2 = driver.find_element(By.CSS_SELECTOR,
                                 "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > label.pwd-show > input").get_attribute(
        'value')
    shouzimu = suiji2[0]
    while is_number(shouzimu):
        driver.find_element(By.CSS_SELECTOR,
                            "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > label.operation > button.refresh").click()
        suiji2 = driver.find_element(By.CSS_SELECTOR,
                                     "#app > section.bg-container > header > ul > li:nth-child(3) > aside > div > label.pwd-show > input").get_attribute(
            'value')
        shouzimu = suiji2[0]
    return suiji, suiji2


def 写入txt(a):
    with open('steam账号.txt', 'a') as st:
        st.write(a)
    st.close()


def 写入邮箱账号(邮箱账号, 邮箱密码):
    邮箱账号 += '@wleizz.com'
    邮箱账号 += '----'
    邮箱账号 += 邮箱密码
    邮箱账号 += '----'
    print(邮箱账号)
    写入txt(邮箱账号)


def 邮箱注册总():
    邮箱账号, 邮箱密码 = 获取随机8位()
    写入邮箱账号(邮箱账号, 邮箱密码)
    邮箱后台登录()
    邮箱注册(邮箱账号, 邮箱密码)
    邮箱账号 += '@wleizz.com'
    return 邮箱账号, 邮箱密码


def mouseClick(img):
    while True:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            break
        sleep(0.1)


def 循环检测(img, time):
    i = 0
    while i < time:
        location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        if location is not None:
            return True
        sleep(1)
        i += 1
    return False


def Steam验证码循环点击():
    re = "images/01.png"
    继续 = "images/03.png"
    人 = "images/04.png"
    展开 = "images/05.png"
    点击 = "images/06.png"

    i = 0
    mouseClick(点击)
    while not 循环检测(展开, 1):

        mouseClick(re)
        sleep(1)
        while i < 5:
            mouseClick(人)
            if 循环检测(继续, 5):
                mouseClick(继续)
                break
            i += 1
        mouseClick(点击)
        i = 0
        sleep(2)


def Steam注册(邮箱账号):
    driver.get("https://store.steampowered.com/join/")
    driver.find_element(By.CSS_SELECTOR,
                        '#email').send_keys(
        邮箱账号)
    driver.find_element(By.CSS_SELECTOR,
                        '#reenter_email').send_keys(
        邮箱账号)
    driver.find_element(By.CSS_SELECTOR,
                        "#i_agree_check").click()
    Steam验证码循环点击()


def 邮箱登录(邮箱账号, 邮箱密码):
    js = 'window.open("http://mail.wleizz.com/");'
    driver.execute_script(js)
    drivers = driver.window_handles
    driver.switch_to.window(drivers[-1])
    driver.find_element(By.CSS_SELECTOR,
                        '#rcmloginuser').send_keys(
        邮箱账号)
    driver.find_element(By.CSS_SELECTOR,
                        '#rcmloginpwd').send_keys(
        邮箱密码)
    driver.find_element(By.CSS_SELECTOR,
                        "#rcmloginsubmit").click()


if __name__ == "__main__":
    邮箱账号, 邮箱密码 = 邮箱注册总()
    Steam注册(邮箱账号)
    # 邮箱登录(邮箱账号, 邮箱密码)
