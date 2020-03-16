# coding = utf8

from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(5)


driver.get('https://music.163.com/#/discover/toplist?id=2617766278')

try:
    driver.switch_to_frame('contentFrame')
    list = driver.find_elements_by_css_selector('#song-list-pre-cache td')

    for one in list:
        songname = one.text
        print(songname)
except Exception as e:
    print('Error:', e)
finally:
    driver.quit()


