# coding = utf8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import traceback
import time


driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

    # 出发地输入框
    fromele = driver.find_element_by_id('fromStationText')

    # 点击、清除框内的字、以及输入南京南
    fromele.click()
    fromele.clear()
    fromele.send_keys('南京南\n')

    # 目的地输入框
    destination = driver.find_element_by_id('toStationText')

    # 点击、清除框内的字、以及输入杭州
    destination.click()
    destination.clear()
    destination.send_keys('杭州东\n')


    # 选择时间
    timeselected = Select(driver.find_element_by_id('cc_start_time'))
    timeselected.select_by_visible_text('06:00--12:00')

    tomorrow = driver.find_element_by_css_selector('#date_range >ul>li:nth-child(2)')
    tomorrow.click()

    carnum = driver.find_elements_by_xpath("//*[@id ='t-list']/table/tbody/tr/td[4][@class]/../td[1]//a")

    for one in carnum:
        print(one.text)


except:
    print('ERROR:\n' + traceback.format_exc())

finally:
    input("输入之后结束:")
    driver.quit()




