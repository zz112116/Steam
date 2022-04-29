import random
from time import sleep
from func_timeout import func_set_timeout
import func_timeout
from selenium import webdriver
from selenium.webdriver.common.by import By

# -------------------------------------------------等待提交------------------------------------------------------------------
def 判读元素是否存在(driver, 元素):
    while True:
        try:
            driver.find_element(By.XPATH, 元素)
            return
        except:
            pass


@func_set_timeout(180)
def 等待提交(driver):
    iframe_xpath = '/html/body/div[1]/div[7]/div[5]/div/div[1]/div[2]/form/div/div/div[5]/div/div[1]/div/div/div/iframe'
    对错_xpath = '/html/body/div[2]/div[3]/div[1]/div/div/span'

    判读元素是否存在(driver, iframe_xpath)
    # 切换到iframe
    iframe = driver.find_element(By.XPATH, iframe_xpath)
    driver.switch_to.frame(iframe)
    判读元素是否存在(driver, 对错_xpath)
    元素 = driver.find_element(By.XPATH, 对错_xpath)
    while True:

        if 元素.get_attribute("aria-checked") == 'true':
            print('点击提交')
            break

    # 退出iframe
    driver.switch_to.default_content()
    # 提交
    sleep(1.2)
    action = webdriver.ActionChains(driver)
    moreLink = driver.find_element(By.CSS_SELECTOR, '#createAccountButton')
    action.move_to_element(moreLink).click(moreLink).perform()


# -------------------------------------------------失败之后打印信息------------------------------------------------------------------
@func_set_timeout(2)
def 失败之后打印信息(driver):
    错误_css = '#error_display'
    while True:
        try:
            print('----------------------------------------')
            elements = driver.find_elements(By.CSS_SELECTOR, 错误_css)
            for element in elements:
                print(element.text)
                if element.text == 'There was a problem creating your Steam account, please try again later.':
                    print('----------------------------------------')
                    return '次数到了'
                if element.text == 'You must agree to the Steam Subscriber Agreement to continue.':
                    print('----------------------------------------')
                    return '没点我同意'
                if element.text == 'Please enter a valid email address.':
                    print('----------------------------------------')
                    return '没填邮箱'
            print('----------------------------------------')
            break
        except:
            sleep(0.1)


# -----------------------------------------------判断是否成功--------------------------------------------------------------------
@func_set_timeout(5)
def 判断成功(driver):
    成功_css = '#email_verification_dialog'
    while True:
        元素 = driver.find_element(By.CSS_SELECTOR, 成功_css)
        if 元素.get_attribute("style") == '':
            print('----------------------------------------')
            elements = driver.find_elements(By.CSS_SELECTOR, 成功_css)
            for element in elements:
                print(element.text)
            print('----------------------------------------')
            return '成功'


def 邮箱是否成功(driver):
    try:
        是否成功 = 判断成功(driver)
    except func_timeout.exceptions.FunctionTimedOut:
        是否成功 = '失败'

    if 是否成功 == '失败':
        try:
            是否成功 = 失败之后打印信息(driver)
            if 是否成功 == None:
                return '错误代码'
            return 是否成功
        except func_timeout.exceptions.FunctionTimedOut:
            return '未知错误'
    return 是否成功


# --------------------------------------------------逻辑总-----------------------------------------------------------------
def 等待验证之后(driver, 当前窗口句柄):
    try:
        等待提交(driver)
    except func_timeout.exceptions.FunctionTimedOut:
        print('等待验证码超时')
        是否成功 = '等待验证码超时'
        return 是否成功, 当前窗口句柄
    except:
        是否成功 = '等待验证码异常'
        return 是否成功, 当前窗口句柄
    是否成功 = 邮箱是否成功(driver)
    return 是否成功


if __name__ == "__main__":
    # 等待验证之后提交(driver)
    pass
