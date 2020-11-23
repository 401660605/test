# coding:utf8
from selenium import webdriver
import web, time

driver = web.open_browser()
web.get('http://www.5gegg.cn')
web.input('//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[1]/input', 'wlj')
web.input('//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[2]/input', '123567')
web.input('//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[3]/input', '1')
web.click('//*[@id="app"]/div/div/div[2]/div[1]/div[2]/button')
time.sleep(1)
text = web.get_text('//*[@id="app"]/div/div/div[2]/div[1]/div[3]/span[1]')
web.assert_equals('{text}','王丽娟欢迎您~')
