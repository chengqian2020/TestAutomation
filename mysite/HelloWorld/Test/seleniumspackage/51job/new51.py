# coding = utf8

from selenium import webdriver
import traceback
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('https://www.51job.com/')

# 点击高级搜索
driver.find_element_by_css_selector('div>div>a[class=more]').click()
# 输入python
driver.find_element_by_id('kwdselectid').send_keys('python')
# 点击选择南京页面
driver.find_element_by_id('work_position_input').click()

# 保持界面稳定
time.sleep(1)
# 找出是on的元素
onelement = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')

try:
    for one in onelement:
        one.click()
    # 点击选择南京
    driver.find_element_by_id('work_position_click_center_right_list_category_000000_070200').click()
    # 点击确认
    driver.find_element_by_id('work_position_click_bottom_save').click()
    driver.find_element_by_class_name('tit').click()
    # 点击职能类别
    driver.find_element_by_id('funtype_click').click()
    # 点击计算机专业
    driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
    # 点击高级软件工程师
    driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
    # 点击确定
    driver.find_element_by_id('funtype_click_bottom_save').click()

    # # 点击展开公司性质
    driver.find_element_by_id('cottype_list').click()
    # 点击公司性质"#cottype_list>div>span[title=外资（欧美）]"
    driver.find_element_by_css_selector('#cottype_list div>span[title="国企"]').click()
    # 公司性质选 外资 欧美
    # driver.find_element_by_id('cottype_list').click()
    # driver.find_element_by_css_selector('#cottype_list span.li[data-value="01"]').click()

    # #工作年限选择
    driver.find_element_by_id('workyear_list').click()
    driver.find_element_by_css_selector('span[title="1-3年"]').click()

    # # 工作年限选
    # driver.find_element_by_id('workyear_list').click()
    # driver.find_element_by_css_selector('#workyear_list span.li[data-value="02"]').click()

    # 点击搜索
    driver.find_element_by_css_selector('div.d_lt>div>span').click()
    allinfo = driver.find_elements_by_css_selector('#resultList>div[class=el] ')
    for info in allinfo:
        fileds = info.find_elements_by_tag_name('span')
        strinfo = [filed.text for filed in fileds]
        print(' | '.join(strinfo))


except:
    print('ERROR:\n' + traceback.format_exc())
finally:
    time.sleep(5)
    driver.quit()










