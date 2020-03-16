# coding = utf8
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('/Users/cq/Django/mysite/HelloWorld/Test/seleniumspackage/HTMLfile/gouxuankuang.html')

Html = driver.find_element_by_css_selector('div input')

print(Html.get_attribute('outerHTML'))


driver.quit()