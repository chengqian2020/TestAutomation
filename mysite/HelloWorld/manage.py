# coding = utf8
from selenium import webdriver
import traceback

def champzee():
    driver = webdriver.Chrome()

    driver.implicitly_wait(5)

    driver.get('https://www.champzee.com/m/login')

    try:

        driver.find_element_by_css_selector('div[class=operation-item]>div').click()

        driver.find_element_by_css_selector('div>input[placeholder="请输入手机号"]').send_keys('15750888250')

        driver.find_element_by_css_selector('div>input[placeholder="请输入密码"]').send_keys('woxiangnile')

        driver.find_element_by_xpath("//*[@id='app']/div//button").click()

    except:
        print("ERROR:" + traceback.format_exc())

    finally:
        input("输入之后代码启动：")
        driver.quit()



