# coding:utf-8
import unittest
import time
from selenium import webdriver
# from sys import path
# path.append(r'.\models')
# from .models import picReco

class loginTestCase(unittest.TestCase):
    def setUp(self):
        baseurl = 'http://54.223.152.8:8088/duty/'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseurl)
        assert self.driver.title, 'Schedule'
        time.sleep(2)
    def test_login_success(self):
        ele_name = self.driver.find_element_by_xpath('//*[@id="loginname"]')
        ele_name.clear()
        ele_name.send_keys('shouqian')
        ele_pwd = self.driver.find_element_by_xpath('//*[@id="password"]')
        ele_pwd.clear()
        ele_pwd.send_keys('123ewq')

        ele_code = self.driver.find_element_by_xpath('//*[@id="codeImg"]')

        captcha = loginTestCase.get_auth_code(ele_code)
        time.sleep(1)

        print(captcha)

        # ele_capt = self.driver.find_element_by_xpath('//*[@id="code"]')
        # ele_capt.clear()
        # ele_capt.send_keys(captcha)
        # time.sleep(2)
        # ele_butt = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[6]/div')
        # ele_butt.click()
        # time.sleep(2)
        # ele_welcome = self.driver.find_element_by_xpath('//*[@id="user_info"]')
        # assert self.driver.title, 'Visit calendar'
        # assert ele_welcome.text, '田帆'

    def get_auth_code(self, codeEelement):
        '''获取验证码'''
        self.driver.save_screenshot('F:\Code\PyCharm\AutomatedAndInterface\Auto_Duty\Duty\data\img\login.png')  # 截取登录页面
        imgSize = codeEelement.size  # 获取验证码图片的大小
        imgLocation = imgElement.location  # 获取验证码元素坐标
        rangle = (int(imgLocation['x']), int(imgLocation['y']), int(imgLocation['x'] + imgSize['width']),
                  int(imgLocation['y'] + imgSize['height']))  # 计算验证码整体坐标
        login = Image.open("login/login.png")
        frame4 = login.crop(rangle)  # 截取验证码图片
        frame4.save(r'F:\Code\PyCharm\AutomatedAndInterface\Auto_Duty\Duty\data\img\authcode.png')
        authcodeImg = Image.open(r'F:\Code\PyCharm\AutomatedAndInterface\Auto_Duty\Duty\data\img\authcode.png')
        authCodeText = pytesseract.image_to_string(authcodeImg).strip()
        return authCodeText

    # def tearDown(self):
        # self.driver.quit()
if __name__ == '__main__':
    unittest.main()
