
import PIL
from PIL.Image import Image
from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.chrome.options import Options


import requests
from hashlib import md5


#超级鹰区域
class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        print(r)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64':base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()






#selenium识别验证码并提交
def start():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
             'AppleWebKit/537.36 (KHTML, like Gecko)'
             'Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'}
    #chrome_options = Options()
    #chrome_options.add_argument()
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    dirver=webdriver.Chrome(chrome_options=option)

    #打开推广链接
    dirver.get("https://iake.hnzmt.cn/?i=FIiz4L")
    dirver.maximize_window()

    #定位验证码和输入框
    dirver.find_element("xpath",'//*[@id="submit_code"]')
    dirver.find_element("xpath",'//*[@id="codeimg"]')

    #全屏截图
    dirver.save_screenshot('page.png')
    code_img_ele = dirver.find_element("xpath",'//*[@id="codeimg"]')
    # 获取验证码左上角的坐标x,y
    location = code_img_ele.location

    size = code_img_ele.size
    #range=(
    #    int(location['y'])*1.5,int(location['y']+size['height'])*1.5,int(location['x'])*1.5,int(location['x']+size['width'])*1.5
    #)
    range=(731,388,897,453)

    i = PIL.Image.open('./page.png')
    """定点切割，不计算坐标
    #code_img_name = './code.png'
    # crop根据rangle元组内的坐标进行裁剪#
    """

    frame = i.crop(range)
    frame.save("./final_image.png")


    #超级鹰脚本
    chaojiying = Chaojiying_Client('账号', '密码', '密钥')
    im = open('./final_image.png', 'rb').read()
    print (chaojiying.PostPic(im, 8001)	)

    #接收超级鹰返回验证码
    code=chaojiying.PostPic(im,8001)['pic_str']
    #删掉截图
    os.remove("./final_image.png")

    #模拟输入
    code_input = dirver.find_element("xpath", '//*[@class="form-control input-lg"]')
    code_input.send_keys(code)

    #定位提交键，模拟点击
    button=dirver.find_element("xpath",'//*[@id="submit_code"]')
    button.click()
    sleep(5)
    dirver.quit()
    dirver.close()
    sleep(10)


while True:
    try:
        start()
    except:
        pass



