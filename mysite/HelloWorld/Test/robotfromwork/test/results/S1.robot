*** Settings ***
Library  Selenium2Library

*** Test Cases ***
Test1
    ${var1}=    convert to integer  100
    ${var2}=    set variable  50
    should be true  $var1 * int($var2) == 5000

Test2
    [Documentation]                 登录百度搜索"北京时间"
    Open Browser                    http://www.baidu.com    chrome
    Set Selenium Implicit Wait      5
    Input Text                      id = kw     北京时间\n
    ${time}=                        Get Text        css=p>span[class=op-beijingtime-date]
    log to console                  ${time}
    should be true                  $time.startswith('2020')
    Close Browser


Test3
    [Documentation]                 登录垂衣
    Open Browser                    https://www.champzee.com/m/login    chrome
    Set Selenium Implicit Wait      5
    Close Browser




