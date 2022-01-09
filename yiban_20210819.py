# -*- coding: utf8 -*-
import requests
import time
import re
import logging

'''
cron:  50 7 * * * yiban_20210819.py
new Env('易班打卡');
'''

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

kutui_sckey = '0f25fa468121492daa756d07d5af4c13'
sckey = 'SCT1450TJ4BtzkQZuaGEGzGAhYtFmquM'
mbr = 'XiaSongmin'
msg = ('湖南省','怀化市','新晃侗族治自县','419200','湖南省 怀化市 新晃侗族治自县','17674534215','1841601149')
url = 'http://smart.hnsyu.net/xyt/wx/index/loginSubmit.do'
url1 = 'http://smart.hnsyu.net/xyt/wx/health/toApply.do'
url2 = 'http://smart.hnsyu.net/xyt/wx/health/saveApply.do'
url3 = 'http://smart.hnsyu.net/xyt/wx/health/main.do'
headers = {
        'Origin': 'http://smart.hnsyu.net',
        'Referer': 'http://smart.hnsyu.net/xyt/home/login.do;jsessionid=554A3171A5DFBC002BF3383D6EC27EE7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}
headers1 = {
    'Host': 'smart.hnsyu.net',
    'Referer': 'http://smart.hnsyu.net/xyt/wx/health/toApply.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}
headers2 = {
    'Referer': 'http://smart.hnsyu.net/xyt/wx/health/toApply.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}
class WxPush():
    def __init__(self):
        self.corpid = 'ww7aa45d1915be80d0'  # 企业id
        self.agentid = 1000003  # 应用ID
        self.corpsecret = 'zov0_wqraq8--BWhSoPwYw0G9KViMqH2rw9TNqOHg4w'  # 应用密钥
        self.mbr = mbr# 成员ID，默认@all,MeiYouNiCheng

    def push_main(self,content):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + self.corpid + '&corpsecret=' + self.corpsecret).json()
        access_token = r['access_token']
        print(access_token)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
        json = {
            "touser": self.mbr,
            "toparty": "@all",  # 部门
            "totag": "@all",  # 标签
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {
                "content": content
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        r1 = requests.post(url=url, json=json)

class SignIn():
    num = 0
    def start(self,province,city,district,adcode,add,tel,ID):
        data = {'username': ID,'password': ID,}
        s = requests.Session()
        s.post(url, headers=headers, data=data)
        r1 = s.get(url1, headers=headers1)
        reg = r'[a-zA-Z0-9]{8}\D[a-zA-Z0-9]{4}\D[a-zA-Z0-9]{4}\D[a-zA-Z0-9]{4}\D[a-zA-Z0-9]{12}'
        ttoken = re.compile(reg).findall(r1.text)
        if ttoken != []:
            data1 = {
                'ttoken': ttoken[0],
                'province': province,# 省
                'city': city,# 市
                'district': district,# 县
                'adcode': adcode,# 邮编
                'longitude': '0',
                'latitude': '0',
                'sfqz': '否',
                'sfys': '否',
                'sfzy': '否',
                'sfgl': '否',
                'status': '1',
                'sfgr': '否',
                'szdz': add,
                'sjh': tel,
                'lxrxm': '',
                'lxrsjh': '',
                'sffr': '否',
                'sffy': '否',
                'qzglsj': '',
                'qzgldd': '',
                'glyy': '',
                'mqzz': '',
                'sffx': '否',
                'qt': '',
            }
            r_sign = s.post(url2, headers=headers2, data=data1)
            content = eval(r_sign.text)['msgText'] + eval(r_sign.text)['msgStatus'] + '\n\n' + time.strftime('%Y-%m-%d %X')
            return content
        else:
            r3 = s.get(url3)
            inform_a = (re.compile(r'(?<=<span class="normal-sm-tip green-warn fn-ml10">).+(?=</span>)').findall(r3.text))[0]
            inform_b = (re.compile(r'(?<=<div class="weui-cell__bd normal-font fn-ar fc-gray2">).{10}(?=</div>)').findall(r1.text))[0]
            content = inform_a + '\n\n' + '上报时间：' + inform_b
            return content

def main():
    try:
        signin = SignIn()
        content = signin.start(msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6])
        # push = WxPush()
        # push.push_main(content)
        requests.get('https://telechan-mu.vercel.app/api/send?sendkey=629979069Tec01f1a418f8781346788d6f468499ec&text=' + content)
        # requests.get('http://www.pushplus.plus/send?token=' + kutui_sckey + '&title=易班打卡成功&content=' + content + '&template=html')
        logger.info(content)
    except:
        print('网络错误') # 不知道怎么处理错误
        content = '网络错误，手动登录查看' + '\n\n' + 'http://smart.hnsyu.net/xyt/home/login.do'
        logger.info(content)
        requests.get('https://telechan-mu.vercel.app/api/send?sendkey=629979069Tec01f1a418f8781346788d6f468499ec&text=' + content)
        push = WxPush()
        push.push_main(content)

def main_handler(event, context):
    main()
if __name__=="__main__":
    main()

