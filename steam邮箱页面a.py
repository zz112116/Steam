from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from func_timeout import func_set_timeout
import func_timeout

from adspower接口调用 import 创建账号, 打开某账号浏览器, 删除账号, 关闭某账号浏览器, 判断账号是否打开
from 新建邮箱 import 邮箱注册
from 等待验证通过 import 邮箱是否成功, 等待验证之后, 等待提交
# win32clipboard专门用来复制粘贴的


from 验证码识别 import 点击验证码全


# ------------------------------------输入邮箱账号---------------------------------------
def 输入邮箱账号(driver, 邮箱账号):
    # 复制内容(邮箱账号)
    element_obj = driver.find_element(By.CSS_SELECTOR, '#email')
    element_obj2 = driver.find_element(By.CSS_SELECTOR, '#reenter_email')
    element_obj.click()
    for i in 邮箱账号:
        ActionChains(driver).key_down(i).key_up(i).perform()
    element_obj2.click()
    for i in 邮箱账号:
        ActionChains(driver).key_down(i).key_up(i).perform()


# ------------------------------------------------------------------------------------------

# ------------------------------------点击我同意---------------------------------------
@func_set_timeout(10)
def 点击我同意(driver):
    while True:
        driver.find_element(By.CSS_SELECTOR, "#i_agree_check").click()
        break

# ------------------------------------------------------------------------------------------


# ------------------------------------逻辑总------------------------------------------------


def 等待验证之前(driver, 邮箱账号):
    try:
        driver.get('https://store.steampowered.com/join/')
        当前窗口句柄 = driver.current_window_handle
    except:
        是否成功 = 3
        print('打开页面失败，可能是代理ip出问题')
        return 是否成功, 当前窗口句柄
    点击我同意(driver)
    driver.switch_to.window(当前窗口句柄)
    输入邮箱账号(driver, 邮箱账号)
    return 当前窗口句柄


def 邮箱页面操作(driver, 邮箱账号):
    当前窗口句柄 = 等待验证之前(driver, 邮箱账号)
    是否成功 = 等待验证之后(driver, 当前窗口句柄)
    return 是否成功, 当前窗口句柄


# ------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # 是否成功 = steam邮箱页面()
    pass
