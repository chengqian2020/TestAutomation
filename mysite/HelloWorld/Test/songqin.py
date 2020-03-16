# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.implicitly_wait(10)

baidu = 'http://www.baidu.com'

driver.get(baidu)
driver.find_element_by_id('kw').send_keys('松勤')

driver.find_element_by_id('su').click()


ele = driver.find_element_by_id('1')

if ele.text.startswith('松勤网 - 松勤软件测试-软件测试在线教育领跑者-国内最专业的软件...'):
    print('pass')
else:
    print('fail')




driver.quit()


# # 获取某个属性的值
# resulet = ele.get_attribute('href')
# # 该元素对应的html源码
# resulet1 =
#
# # 该元素的内部部分的html源代码
# resulet2 = ele.get_attribute('innerHTML')
#
# print(resulet1)

# 获取标题
driver.title
# 获取url
driver.current_url
# 切换窗口
allwindows = driver.window_handles

for one in driver.window_handles:       #循环遍历所有窗口
    driver.switch_to.window(one)        # 切到该窗口

    if 'title' in driver.title:         # 如果该窗口标题为需要操作的title，那么停止循环
        break

# 对话框操作
driver.switch_to.alert.accept()         #点击弹窗
driver.switch_to.alert.text             #得到对话框内容
driver.switch_to.alert.dismiss()        #点击cancel
driver.switch_to.alert.send_keys('内容')      #输入内容

#刷新页面
driver.refresh()
#前进页面
driver.forward()
#后退页面
driver.back()