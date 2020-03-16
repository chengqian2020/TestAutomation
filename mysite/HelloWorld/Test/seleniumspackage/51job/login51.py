# coding = utf8
import time
from selenium import webdriver
import traceback

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.51job.com/')

driver.find_element_by_id('kwdselectid').send_keys('python')


driver.find_element_by_id('work_position_input').click()

# cityinfo = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')
cityinfos = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')

try:
    for one in cityinfos:
        one.click()
    driver.find_element_by_css_selector('#work_position_click_center_right_list_category_000000_070200')
    # for one in cityinfo:
    #     cityname = one.text
    #     selected = one.get_attribute('class')

        # if cityname == "南京":
        #     if selected != 'on':
        #         one.click()
        # else:
        #     if selected == 'on':
        #         one.click()

    driver.find_element_by_id('work_position_click_bottom_save').click()

    driver.find_element_by_css_selector('.ush button').click()


    jobs = driver.find_elements_by_css_selector("#resultList div[class=el]")

    for job in jobs:
        # if 'title' in job.get_attribute('class'):
        #     continue
        fileds = job.find_elements_by_tag_name('span')
        strfiled = [filed.text for filed in fileds]
        print(' | '.join(strfiled))



except :
    print('Error:\n' + \
          traceback.format_exc())

finally:
    driver.quit()




