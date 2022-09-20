import settings
from time import sleep
import random
import requests

jusk_dict={
    "(+[]+[])": "0",
	"(+!![]+[])": "1",
	"(!+[]+!![]+[])": "2",
	"(!+[]+!![]+!![]+[])": "3",
	"(!+[]+!![]+!![]+!![]+[])": "4",
	"(!+[]+!![]+!![]+!![]+!![]+[])": "5",
	"(!+[]+!![]+!![]+!![]+!![]+!![]+[])": "6",
	"(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])": "7",
    "(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])": "8",
    "(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])": "9",
    "(+{}+[])[+!![]]": "a",
	"([]+{})[!+[]+!![]]": "b",
	"([]+{})[!+[]+!![]+!![]+!![]+!![]]": "c",
	"([][[]]+[])[!+[]+!![]]": "d",
    "([][[]]+[])[!+[]+!![]+!![]]": "e",
    "(![]+[])[+[]]": "f"
}
"""
模块分解：
ip   换ip
rq_get_jf 提交request获得jsfuck模块
re_get_img request获得照片模块
img_code 识别照片获得验证码模块
img_code  识别照片获得验证码模块
jf_cookie 计算jsfuck
send_code 返回验证码
"""
header_get= {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.366"}


html_kuaiip="https://dps.kdlapi.com/api/getdps/?secret_id=obzhk9ccqbifnujfl4nk&num=20&signature=ouuoo6ya092mt14o9ztj5yyvko&pt=1&sep=1"

code_url=input("（例如：https://iake.hnzmt.cn/?i=5Pzt14中5Pzt14是所需要输入的）\n请输入你的链接:\n")

num=int(input("请输入你的推广次数：\n"))
n=0
n1=0
html_ip='http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=94b4cb54a1ee4c53b9e5637f6a85f0d5&orderno=YZ202291331597klpRL&returnType=1&count=20'
ip_post_text=requests.get(url=html_ip).text
ip_post_list=ip_post_text.split('\r\n')
succ_num=0

while n<num:
    try:
        sleep_num=random.randint(1,4)
        sleep(sleep_num)
        proxy = settings.ip(ip_post_list,n1)
        if n1==5:
            html_ip = html_kuaiip
            ip_post_text = requests.get(url=html_ip).text
            ip_post_list = ip_post_text.split('\r\n')
            n1=0
        n1=n1+1
        cookie_php_dict,jsfuck=settings.rq_get_jf(header_get,proxy)
        if cookie_php_dict==0 or jsfuck==0:
            cookie = None
            continue
        else:
            sec_defend=settings.jf_cookie(jsfuck,jusk_dict)
            cookie="PHPSESSID="+cookie_php_dict+";sec_defend="+sec_defend+";sec_defend_time=1;"
            img_get = settings.re_get_img(cookie)
            code = settings.img_code()
            code_sent_respone=settings.send_code(cookie,code_url,code,proxy,succ_num)
            print(code_sent_respone)
            if code_sent_respone['msg']=='succ':
                n=n+1
                print("第",n,'次成功')
            cookie=None
            print()
    except:
        print('出错')
        cookie=None
        pass
