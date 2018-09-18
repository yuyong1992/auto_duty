import sys
from sys import path
path.append(0, sys.path[0]+'\\models')
from .models.WebDriverMethod import SeleniumMethod

class loginPage(SeleniumMethod):
    # 登录页面对象
    username = '//*[@id="loginname"]'
    # 用户名输入框
    password = '//*[@id="password"]'
    # 密码输入框
    captcha = '//*[@id="code"]'
    # 验证码输入框
    button = '//*[@id="loginForm"]/div[6]/div'
    # 登录按钮
    pageTitle = 'Shedule'