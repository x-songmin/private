# -*- coding: utf8 -*-
import requests
import time
import re
import logging
import random
from wxpush import WxPush
'''
cron:  20 7 * * *
new Env('xsm_易班打卡');
'''
#日志输出
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)
#推送参数
kutui_sckey = '0f25fa468121492daa756d07d5af4c13'
sckey = 'SCT1450TJ4BtzkQZuaGEGzGAhYtFmquM'
mbr = 'XiaSongmin'
# 打卡个人数据
# eg：['省','市','县','邮编','省 市 县（空格隔开）','电话号码','学号']
msgs = (
    ['湖南省','怀化市','新晃侗族治自县','419200','湖南省 怀化市 新晃侗族治自县','17674534215','1841601149'],
    # ['湖南省','邵阳市','武冈县','422400','湖南省 邵阳市 武冈县','17673936070','1841601144']
)
#请求数据
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
# 突然发现headers1和2一样的
headers2 = {
    'Referer': 'http://smart.hnsyu.net/xyt/wx/health/toApply.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}

# 企业微信推送
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
# 主程序
class SignIn():
    num = 0 # 忘记之前用来干啥的了
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
            s.get(url='http://smart.hnsyu.net/xyt/wx/index/logout.do',headers=headers2) # 退出登录
            return content
        else:
            r3 = s.get(url3)
            inform_a = (re.compile(r'(?<=<span class="normal-sm-tip green-warn fn-ml10">).+(?=</span>)').findall(r3.text))[0]
            inform_b = (re.compile(r'(?<=<div class="weui-cell__bd normal-font fn-ar fc-gray2">).{10}(?=</div>)').findall(r1.text))[0]
            content = inform_a + '\n\n' + '上报时间：' + inform_b
            s.get(url='http://smart.hnsyu.net/xyt/wx/index/logout.do',headers=headers2)
            return content
        

# 运行
def main():
    num = 0
    for msg in msgs[0:] :
        try:
            signin = SignIn()
            num +=1
            content = signin.start(msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6])
            logger.info(content)
            sleep = random.randint(5,11)
            print('暂停' + str(sleep) + '秒')
            time.sleep(sleep)
            content = content + '\n' + '第' + str(num) + '个账号完成' + str(msg[6] + '\n' + '==========================================================' + '\n')
            push = WxPush()
            push.push_main(content)
#             requests.get('https://telechan-mu.vercel.app/api/send?sendkey=629979069Tec01f1a418f8781346788d6f468499ec&text=' + content)
            # requests.get('http://www.pushplus.plus/send?token=' + kutui_sckey + '&title=易班打卡成功&content=' + content + '&template=html')
            logger.info('第' + str(num) + '个账号完成' + str(msg[6]) + '\n\n' + '==========================================================')
            # print('第' + str(num) + '个账号完成' + str(msg[6]) + '\n\n' + '==========================================================')
        except:
            print('网络错误') # 不知道怎么处理错误
            news = '第' + str(num) + '个账号错误' + str(msg[6])
            content = '网络错误，手动登录查看:' + news + '\n\n' + 'http://smart.hnsyu.net/xyt/home/login.do'
            logger.info(content)
#             requests.get('https://telechan-mu.vercel.app/api/send?sendkey=629979069Tec01f1a418f8781346788d6f468499ec&text=' + content)
            push = WxPush()
            push.push_main(content)
            push = WxPush()
            push.push_main(content)

def main_handler(event, context):
    main()
if __name__=="__main__":
    main()

