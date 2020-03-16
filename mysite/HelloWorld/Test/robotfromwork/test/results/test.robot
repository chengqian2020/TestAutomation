*** Settings ***
Library  SeleniumLibrary
Library  Dialogs

*** Test Cases ***
#百度搜索松勤
#    Open Browser                  http://www.baidu.com    chrome
#    Set Selenium Implicit Wait    5
#    Input Text                    id=kw                   松勤\n
#    ${firstRet}=                  Get Text                id=1
#    Should Contain                ${firstRet}             松勤网
#    Close Browser

测试1
    [Documentation]     测试初始化 清除
    [Setup]             log to console      \n  *** 我是开始 ***
    log to console      chengqian
    [Teardown]          log to console      \n  *** 我是结束 ***

测试2
    log to console  我就是我


