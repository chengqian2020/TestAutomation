# coding = utf8

from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get('http://music.taihe.com/top/new')


# div = driver.find_element_by_id('songListWrapper')
# ul = div.find_element_by_tag_name('ul')
# li = ul.find_elements_by_tag_name('li')

li = driver.find_elements_by_css_selector('#songListWrapper ul li')

for one in li:
    uptag = one.find_elements_by_class_name('up')
    if uptag != []:
        title = one.find_element_by_class_name('song-title ')
        titlestr = title.find_element_by_tag_name('a').text
        # print(titlestr)

        name = one.find_element_by_class_name('author_list').text
        # print(name)

        songlists = (f'{titlestr:15s}:{name}')
        print(songlists)




driver.quit()



