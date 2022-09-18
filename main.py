import settings
from time import sleep
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
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
             "AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/89.0.4389.90 Safari/537.36"}



proxy=settings.ip()
code_url=input("（例如：https://iake.hnzmt.cn/?i=5Pzt14中5Pzt14是所需要输入的）\n请输入你的链接:\n")
html="https://iake.hnzmt.cn/?i="+code_url
num=int(input("请输入你的推广次数：\n"))
n=0
while n<num:
    n=n+1
    cookie_php_dict,jsfuck=settings.rq_get_jf(html,header_get,proxy)
    if cookie_php_dict==0 or jsfuck==0:
        continue
    else:
        sleep(3)


        sec_defend=settings.jf_cookie(jsfuck,jusk_dict)
        cookie="PHPSESSID="+cookie_php_dict+";sec_defend="+sec_defend+";sec_defend_time=1;"
        code = settings.img_code()
        img_get=settings.re_get_img(cookie)
        code_sent_respone=settings.send_code(cookie,code_url,code,proxy)
        print(code_sent_respone)