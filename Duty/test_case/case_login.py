# coding=utf-8

import time
from selenium import webdriver
from PIL import Image,ImageEnhance
import pytesseract

def get_auth_code(driver, code_element):
    # driver = webdriver.Chrome()
    driver.save_screenshot('../data/img/login.png')
    imgSize = code_element.size
    imgLocation = code_element.location
    rangle = (int(imgLocation['x']), int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']), int(imgLocation['y'] + imgSize['height']))
    login = Image.open('../data/img/login.png')
    img = login.crop(rangle)
    img.save('../data/img/auth_code.png')
    img_code = Image.open('../data/img/auth_code.png')
    text_code = pytesseract.image_to_string(img_code).strip()
    return text_code
def duty_login(driver, uname, pwd, code):
    try:
        ele_name = driver.find_element_by_xpath('//*[@id="loginname"]')
        ele_name.clear()
        ele_name.send_keys(uname)
        ele_pwd = driver.find_element_by_xpath('//*[@id="password"]')
        ele_pwd.clear()
        ele_pwd.send_keys(pwd)
        ele_capt = driver.find_element_by_xpath('//*[@id="code"]')
        ele_capt.clear()
        ele_capt.send_keys(code)
        time.sleep(2)
        ele_butt = driver.find_element_by_xpath('//*[@id="loginForm"]/div[6]/div')
        ele_butt.click()
        time.sleep(2)
        ele_welcome = driver.find_element_by_xpath('//*[@id="user_info"]')
    except Exception as err3:
        print('登录失败')
        print(err3)
    try:
        assert driver.title == 'Visit calendar'
        print('页面标题正确')
    except AssertionError as err:
        print('页面标题错误：')
        print(err)
    try:
        assert ele_welcome.text == 'Welcome\n田fan'
        print('用户姓名正确')
    except AssertionError as err2:
        print('用户名称错误：')
        print(err2)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://54.223.152.8:8088/duty/')
    code_element = driver.find_element_by_xpath('//*[@id="codeImg"]')
    code = get_auth_code(driver, code_element)
    duty_login(driver, 'shouqian', '123ewq', code)
    time.sleep(3)
    driver.quit()