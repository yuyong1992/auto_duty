# coding:utf-8
from PIL import Image
import pytesseract
import urllib.request


# 下载验证码图片到本地
def get_code(codeurl):
    urllib.request.urlretrieve(codeurl, r'F:\Code\PyCharm\AutomatedAndInterface\Auto_Duty\Duty\data\img\code.jpg')

# 识别图片内容
def img_recog():
    # img = '../../data/img/code.jpg'
    img = 'F:\Code\PyCharm\AutomatedAndInterface\Auto_Duty\Duty\data\img\code.jpg'
    text = pytesseract.image_to_string(Image.open(img), lang='chi_sim')
    # text2 = pytesseract.image_to_string(Image.open(img))
    return text
    # print(text)
    # print(text2)

def get_auth_code(driver, codeEelement):
    '''获取验证码'''
    driver.save_screenshot('F:\Code\PyCharm\AutomatedAndInterface\Auto_Duty\Duty\data\img\login.png')  # 截取登录页面
    imgSize = codeEelement.size  # 获取验证码图片的大小
    imgLocation = imgElement.location  # 获取验证码元素坐标
    rangle = (int(imgLocation['x']), int(imgLocation['y']), int(imgLocation['x'] + imgSize['width']),
              int(imgLocation['y'] + imgSize['height']))  # 计算验证码整体坐标
    login = Image.open("login/login.png")
    frame4 = login.crop(rangle)  # 截取验证码图片
    frame4.save('login/authcode.png')
    authcodeImg = Image.open('login/authcode.png')
    authCodeText = pytesseract.image_to_string(authcodeImg).strip()
    return authCodeText