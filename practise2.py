import string
import time
import PIL
from PIL.Image import Image
from selenium import webdriver
from time import sleep
import requests

import os
from threading import Timer
import datetime
import eventlet


N=0

import urllib3

from re import match
from io import BytesIO
from time import time
import base64
import hashlib
import requests


class GetCode():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self):
        self.stamp = str(int(time()))
        self.s = requests.session()
        self.api_url = "http://pred.fateadm.com/api/capreg"  # 图文验证码识别接口

    def calcSign(self, pd_id, passwd, timestamp):
        """
         # MD5加密获取sign
        :param pd_id: 斐斐打码PD账号
        :param passwd: 斐斐打码PD密钥
        :param timestamp: 当前时间戳
        :return: 返回md5加密结果
        """
        md5 = hashlib.md5()
        md5.update((timestamp + passwd).encode())  # 转码后加密
        csign = md5.hexdigest()  # 返回摘要，作为十六进制数据字符串值
        md5 = hashlib.md5()
        md5.update((pd_id + timestamp + csign).encode())
        csign = md5.hexdigest()
        return csign

    def imageBase64(self, image_path):
        """
         #image转换base64
        :param image_path: image路径，本地绝对路径或URL
        :return: 返回base64
        """
        if match(r'^http://', image_path) or match(r'^https://', image_path):  # 判断image路径是否URL
            r = self.s.get(image_path, verify=False)  # 图片保存在内存
            base64_data = base64.b64encode(BytesIO(r.content).read())  # 内存中打开图片并获取图片base64编码
        else:
            with open(image_path, "rb") as f:  # open方式打开本地图片
                base64_data = base64.b64encode(f.read())  # 获取图片转换的base64编码
        return base64_data

    def discernCode(self, pd_id, pd_passwd, code_type, image_path):
        
        headers = {
            "Content-type": "application/x-www-form-urlencoded"  # 参数类型，写死不可修改
        }

        payload = {
            "user_id": pd_id,  # 斐斐账户pd_id
            "timestamp": self.stamp,  # 整数型当前时间戳
            "sign": self.calcSign(pd_id=pd_id, passwd=pd_passwd, timestamp=self.stamp),  # md5加密密钥
            "predict_type": code_type,  # 识别的字符类型(参考斐斐打码文档)
            "img_data": self.imageBase64(image_path)  # 验证码图片转换成的base64
        }

        r = self.s.post(data=payload, url=self.api_url, headers=headers, verify=False)
        return r.json()

def start():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 
             'AppleWebKit/537.36 (KHTML, like Gecko)'
             'Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'}
"""
###################################################################
看这里！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
下面第二行这个https://iake.hnzmt.cn/?i=BoOkvZ是推广链接，改成你自己的
###################################################################
"""
    dirver=webdriver.Edge()
    dirver.get("https://iake.hnzmt.cn/?i=BoOkvZ")
    dirver.maximize_window()
    dirver.find_element("xpath",'//*[@id="submit_code"]')
    dirver.find_element("xpath",'//*[@id="codeimg"]')
    sleep(3)
    dirver.save_screenshot('page.png')
    code_input=dirver.find_element("xpath",'//*[@class="form-control input-lg"]')
    code_img_ele = dirver.find_element("xpath",'//*[@id="codeimg"]')
    # 获取验证码左上角的坐标x,y
    location = code_img_ele.location

    size = code_img_ele.size
    #range=(
    #    int(location['y'])*1.5,int(location['y']+size['height'])*1.5,int(location['x'])*1.5,int(location['x']+size['width'])*1.5
    #)
    range=(731,388,897,453)

    i = PIL.Image.open('./page.png')
    code_img_name = './code.png'
    # crop根据rangle元组内的坐标进行裁剪#
    frame = i.crop(range)
    frame.save("./final_image.png")

"""
#######################################################################################
看着这里！！！！！！！！！！！！！！！！！！！！！！！11
PD id 和PD passwd是在个人中心
##########################################################################################
"""
    ReturnResult=GetCode().discernCode(pd_id="136060", pd_passwd="y+xwDFc3UJtsmrJSe0OZ+zuTj5dyxwhg",
                               code_type="30400",image_path="./final_image.png")
    rspdate=ReturnResult['RspData']
    realdata_list=rspdate.split('"')
    code=realdata_list[3]

    os.remove("./final_image.png")

    code_input.send_keys(code)
    sleep(5)
    button=dirver.find_element("xpath",'//*[@id="submit_code"]')
    sleep(5)
    button.click()
    sleep(7)
    dirver.close()


while N<100:
        N=N+1
        start()


