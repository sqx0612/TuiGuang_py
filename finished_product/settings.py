import requests
from chaojiying import Chaojiying_Client
from time import sleep


#提交request获得jsfuck模块
def rq_get_jf(header_get,proxy):
    try:
        resp=requests.get(url='https://iake.hnzmt.cn:443',headers=header_get,timeout=5,proxies=proxy)
        # 先判断一次返回值是否为200，不是的话直接下一次循环
        resp_status_code=resp.status_code
        if resp_status_code !=200:
            return 0,0
        else:
            cookie_php_jar = resp.cookies
            cookie_php_dict= requests.utils.dict_from_cookiejar(cookie_php_jar)
            cookie_php=cookie_php_dict['PHPSESSID']
            jsfuck_1=resp.text.split("'sec_defend',")
            jsfuck_2=jsfuck_1[1].split(');setCookie')
            jsfuck=jsfuck_2[0]
            return cookie_php,jsfuck
    except:
        return 0, 0

#换ip模块
def ip(ip_post_list,n):
     ip_post=ip_post_list[n]
     proxies = {
         'http':'http://'+ip_post,
         'https': 'http://' + ip_post
 }
     return proxies



#request获得照片模块
def re_get_img(cookie):
    img_html="https://iake.hnzmt.cn/user/code.php?r=%3C?php%20echo%20time();?%3E"
    header_get = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36",
        'cookie': cookie}
    code_img_data = requests.get(url=img_html, headers=header_get)
    code_image_status_code = code_img_data.status_code
    with open('./code_image.jpg', 'wb') as fp:
        fp.write(code_img_data.content)
    return code_img_data.cookies



#识别照片获得验证码模块
def img_code():
    chaojiying = Chaojiying_Client('sqx0612', '987412365.', '5e404f2fa937bdd8619ecb5860371c2a')
    im = open('./code_image.jpg', 'rb').read()
    code = chaojiying.PostPic(im, 8001)['pic_str']
    return code


#计算jsfuck
def jf_cookie(jsfuck,jusk_dict):
    value_one=jsfuck.split('+(')
    value_two = list()
    n = 0
    while n < 64:
        if n == 0:
            n = n + 1
            value_two.append(value_one[0])
            continue
        else:

            new_i = '(' + value_one[n]
            value_two.append(new_i)
            n = n + 1

    num=0
    for i in value_two:
        value_two[num]=jusk_dict[i]
        num=num+1
    sec_defend=''
    for i in value_two:
        sec_defend=sec_defend+i
    return sec_defend

#返回验证码模块
def send_code(cookie,code_url,code,proxy,succ_num):
    sleep(1)
    header_sendcode = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.366",
        "cookie": cookie,
        "Host": "iake.hnzmt.cn",
        "Connection": "keep-alive",
        "Content-Length": "20",
        "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Origin": "https://iake.hnzmt.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://iake.hnzmt.cn/?i"+code_url
        }
    data_code = {"key":code_url, "code": code}
    code_send_html = "https://iake.hnzmt.cn/ajax.php?act=invite_verify"
    code_sent_respone = requests.post(url=code_send_html, headers=header_sendcode, data=data_code,proxies=proxy)
    return code_sent_respone.json()