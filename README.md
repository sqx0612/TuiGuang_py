        2022/09/19 19点32分
今天发现问题所在了，验证码识别不正确，是因为
虽然验证码url是固定的，但是请求的cookie要一致才可以
请求验证码的网站加一个cookie就可以解决了
但是又有一个新的问题
就是网站能识别出我的真实IP地址好像
返回的jsfuck值都是一样的

        2022/09/18 21点01分
现在已经全部完成了
我把jsfuck写成了一个字典，用来翻译
并且把ip的代理api接入了
但是，最重要的是：
被网站管理者发现
网站管理者把验证码改成实时的了
<Response [200]>
{'code': 2, 'msg': '验证码错误！'}
我先去取取经，看看怎么处理这种 request请求一次，但返回两个数据包的情况
或者是破解验证码固定url的验证机制


        2022/09/18 11点01分
现在在回学校的高铁上
目前遇到的问题
我已经知道request返回值里面是jsfuck加密了
我也知道怎么解密
但是
我将request获得的jsfuck传入js解密，然后再传过来的时候
解码不对
js能够成功解码，但是传回python后是unicode编码
我对其解码，就会jsfuck

故障也知道，是python传参的时候，将jsfuck当成str传过去的
并且，python的str和js的str不一样

        2022/09/16 19点23分
已经可以python调用js了
先吃晚饭，吃完饭就把这几个模块整合在一起


网上也搜不到
应该是我学的不够深，现在这个转码属于其他领域的问题，我不会描述，所以搜不到
但是问题还是要解决的
现在的解决办法就是遍历所有jsfuck
无非10个数字和26个英文字母
多爬几次，获得jsfuck，然后在python中写成一个字典




        2022/09/16 17点43分
刚刚洗澡去了，放松了一下思维，捋清了现在的情况
请求头只需要带着sec检测的信息就行，不用mysid也能post成功

         header_code={
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.366",
                    "cookie":"PHPSESSID=d5nd9dhgs8o6cb983879p2b5pp; sec_defend=2d350b6d05a5dc113284db958d935e4ae610a8ca587e0dffc63ada4d7894b23f; sec_defend_time=1;",
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
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://iake.hnzmt.cn/?i=5Pzt14"
                     }

现在我去学一学怎么把js接入python就行了



        2022/09/16 14点50分
{'code': 0, 'msg': 'succ', 'key': '5Pzt14'}
第一次爬虫成功
从0开始，先学会了selenium，但是会出现堆叠
目前堆叠情况还没有处理好
现在用request，成功第一次了

全过程：
1，电脑先发送一次请求
2，服务器返回两个请求包，第一个请求包带有一个cookie值phpsessid，一个的计算公式和一个字符集
    cookie由四个值组成，phpsessid,sec_defend,sec_defend_time和mysid
    其中，sec_defend_time是date，如果超过1秒，则刷新网页.所以固定为1
    
3，第二个请求包里面由cookie的四个值，与本地计算所得数据相对比
    并且还携带验证码的url地址
    该地址是一个固定地址，访问即刷新。但在某一时间范围内，验证码有多个，但是均有效

4，请求头携带sec_的必要信息，data内容为验证码。返回成功即完成一次推广


现在，已经成功解码cookie的算法并且生成成功，但还不知道sec_defend和mysid是什么类型的值
sec_defend是64位，mysid是32位，都是由同一个计算公式计算字符集所得到，但不知道是怎么转码的



        2022/09/15 15点14分
目前写出来了request请求类型的了
分为三部：
第一步，向推广链接发一个空包，建立链接
第二步，识别图文验证码（图文验证码是一个固定url每次进入都不一样。但只要建立连接，输入哪一个验证码都可以，好像同时多个验证码都正确）
第三步，发回data（包括推广短链接和code）

目前的瓶颈，发回data包需要cookie识别，但cookie是js计算出来的
爬虫爬不全，目前正在找加密算法的核心文件


        2022/09/15 10点13分
写了一早上，代码写成屎山了
先搞别的，放松放松思路

预计效果：
接入代理api接口获取代理ip
随机cookie和遍历ip
requests.get请求，用screenshot截屏保存
传给超级鹰识别，接收code
将code发出去，接收验证成功的消息
print一下次数和结果

        2022/09/15  02点20分
完成进度：
已接入api接口，并且加了一个过滤，检测一遍代理再加入代理池
selenium打开浏览器，每一次打开都是新的cookie
返回信息方面：加了一个隐性等待，但是好像运行不了，明天早上起来再看看哪里的bug
并发性的话，目前我用requests识别图片会偏移，好像是屏幕的问题，还没来得及试验
但是requests的主要问题是：不知道包含验证码的请求体内容该怎么写，https的连接

浏览器还是有堆叠，找不到问题所在

明天的方向：
检查一遍代理接入有没有bug
加上timeout
看request.screenshot为什么会偏移
解决堆叠问题


        2022/09/14 20点22分
现在解决了 提交验证码后的系统弹窗无法识别内容
写了一个函数，可以识别弹出框内容
但是浏览器堆叠还是存在，且非常严重
api可以手动操作，用客户端软件设置，但是浏览器堆叠需要有人随时看着，不然成功率会特别低


我现在尝试一下能不能用requests来写，并发，可以提高效率



接下来的方向：
1，接入代理api接口,搭建ip池，不必依赖代理客户端软件的自动换ip
2，学会代码层面随机cookie，提高运行速度
3，识别返回信息。若跳转到网站主页或网络故障，则直接关闭进行下一次循环
4，学习requests请求方式，并且实现并发，提高推广效率


在这里开始
selenium+超级鹰
推广链接刷点击量
一次成功的推广过程：新ip和新cookie打开推广链接，输入图文验证码，提交，跳转到网站主页

目前采用selenium方式（小白一个，还没学会requests和beautifulsoup）
图文验证码依赖超级鹰，直接用已经封装好的

正在学习阶段，所以依然practise，代码未模块化封装，全都写到了一个里面

目前的难点：
没学过html，接收到的返回信息不会处理。例如：代理api接口的返回数据，和提交验证码后的系统弹窗无法识别内容

因为经常换代理，所以网速慢，不会优化。
出现网站无法打开，或cookie或ip未更新直接跳转到主页，无法执行selenium中的关闭命令，导致浏览器堆叠

另外cookie也不会更新，只能靠重启来重置cookie














