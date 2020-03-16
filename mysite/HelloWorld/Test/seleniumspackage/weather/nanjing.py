# coding = utf8
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.weather.com.cn/jiangsu/index.shtml')

ele = driver.find_element_by_id('forecastID')
# print(ele.text)

result = ele.text.split('℃\n')
# print(result)

low = None
lowcitys = []

for one in result:
    one = one.replace('℃', '')
    cityname = one.split('\n')[0]
    print(cityname)
    lowtemp = int(one.split('\n')[1].split('/')[0])
    if low == None:

        low = lowtemp
        lowcitys.append(cityname)

    elif lowtemp < low:

        low = lowtemp
        lowcitys = [cityname]

    elif lowtemp == low:
        lowcitys.append(cityname)



print(f"最低温度为{low}，最低温度城市为{','.join(lowcitys)}")


driver.quit()