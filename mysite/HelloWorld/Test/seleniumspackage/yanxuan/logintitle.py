# coding = utf8
from selenium import webdriver
import time
import traceback

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('https://you.163.com/')

try:
    inputbox = driver.find_element_by_css_selector('div>input[class="yx-cp-searchInput"]')
    # print(default.text)
    # print(default.get_attribute('outerHTML'))
    # print(default.get_attribute('inerHTML'))
    # print(inputbox.get_attribute('value'))
    inputbox.clear()

    inputbox.send_keys('珐琅锅')
    driver.find_element_by_css_selector('#j-yx-cp-m-top span[class=yx-cp-searchButtonName]').click()
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    driver.back()
    driver.find_element_by_css_selector('#widgetDialogContainer div[class="w-close j-close-pop"]').click()
except:
    print("ERROR:\n" + traceback.format_exc())

finally:
    input('请输入：')
    driver.quit()



