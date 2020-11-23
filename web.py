# coding:utf8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import traceback

driver = None
# text={}
def open_browser():
    global driver

    try:
        # 去掉不安全提示
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option("useAutomationExtension", False)
        # option.add_experimental_option("excludeSwitches", ['enable-automation'])
        # driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)
        # driver.maximize_window()
        chrome_options = webdriver.ChromeOptions()
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        chrome_options.add_experimental_option("prefs", prefs)  ##关掉密码弹窗
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        #打开浏览器
        # driver.get("https://www.baidu.com")
        #隐式等待
        driver.implicitly_wait(10)
        if driver is None:
            print('fail')
        else:
            print('浏览器初始化成功')
    except Exception as e:
        print(str(traceback.format_exc()))
        return driver

def get(url):
    global driver
    try:
        driver.get(url)
        print('URL获取成功')
    except Exception as e:
        print('fail')
        print(str(traceback.format_exc()))

def input(xpath, text):
    # text= __getvalue(value)
    global driver
    try:
        ele = driver.find_element_by_xpath(xpath)
        ele.clear()
        ele.send_keys(text)
        print('输入'+text)
    except Exception as e:
        print('输入失败')
        print(str(traceback.format_exc()))

def click(xpath):
    global driver
    try:
        ele = driver.find_element_by_xpath(xpath).click()
        print('点击成功')
    except Exception as e:
        print('点击失败')
        print(str(traceback.format_exc()))


def get_text(xpath):
    global driver #,text
    text=''
    try:
        # text['text'] = driver.find_element_by_xpath(xpath).text
        text = driver.find_element_by_xpath(xpath).text

        print('获取到文本%s' % text)
    except Exception as e:
        print('fail')
        print(str(traceback.format_exc()))

    # return text['text']
    return text

def clear(xpath):
    global driver
    try:
        ele = driver.find_element_by_xpath(xpath)
        ele.clear()
        print('已清空数据')
    except Exception as e:
        print('fail')
        print(str(traceback.format_exc()))

#业务逻辑断言
def assert_equals(key,value):
    # key=__getvalue__(key)
    # value=__getvalue__(value)
    if key == value:
        print('断言一致'+key)
    else:
        print('匹配失败'+key)

#定义一个私有方法
# def __getvalue__(value):
#     global text
#     for key in text.keys():
#         try:
#             value.replace('{'+key+'}',text[key])
#         except Exception as e:
#             pass
#     print(value)
#     return value
# #获取数据后转存
# def set_varible(key,value):
#     global text
#     text[key]=value


