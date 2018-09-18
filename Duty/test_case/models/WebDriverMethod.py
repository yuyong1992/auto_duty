# coding:utf-8
from selenium import webdriver
class SeleniumMethod(object):
    # 封装Selenium常用方法
    def __init__(self, driver):
        # 构造函数
        self.driver = driver
    def getTitle(self):
        # 获取页面标题
        return self.driver.title
    def clearAndInpute(self, location, value):
        # 根据xpath定位输入框并清除内容后输入新内容
        element = self.driver.find_element_by_xpath(location)
        element.clear()
        element.send_keys(value)
    def click(self, location):
        # 根据xpath定位元素并点击
        return self.driver.find_element_by_xpath(location).click
    def getText(self, location):
        # 根据xpath定位元素并获取其文本
        return self.driver.find_element_by_xpath(location).text
