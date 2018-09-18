# coding:utf-8
from PIL import Image
import pytesseract
import urllib.request

class codeReco():
    # 下载验证码图片到本地
    def get_code(self, baseurl, codepath):
        codeurl = baseurl+codepath
        urllib.request.urlretrieve(codeurl, 'F:\Code\PyCharm\AutomatedAndInterface\Auto_Duty\Duty\data\img\code.jpg')

    # 识别图片内容
    def img_recog(self, img):
        # img = '../../data/img/code.jpg'
        self.text = pytesseract.image_to_string(Image.open(img), lang='chi_sim')
        # return text
        print(text)

    # 删除验证码图片

# if __name__ == '__main__':

base_url = 'http://54.223.152.8:8088/duty/'
code_path = 'code.do?t=1536561823531'
img1 = '../../data/img/code.jpg'
codeReco.get_code(base_url, code_path)
codeReco.img_recog(img1)
