import requests,time,re,logging,random
from wxpush import WxPush
#? 有时间改用环境变量
'''
cron:  30 7 * * *
new Env('xsm_疫情打卡_永州');
'''
# 账号数据
from account import accounts_yongzhou
msgs = accounts_yongzhou
# 日志输出
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)
# data时间参数
times = time.strftime('%Y-%m-%d')
# 有时间可以把data也分出去

class SignIn:
    def __init__(self,uname,pd_mm,lxdh) :
        self.uname = uname
        self.lxdh = lxdh
        self.url = 'http://syxyyqfk.hnsyu.net/website/login'
        self.url1 = 'http://syxyyqfk.hnsyu.net/content/student/temp/zzdk?_t_s_='
        self.url2='http://syxyyqfk.hnsyu.net/website/logout'
        self.url3='http://syxyyqfk.hnsyu.net/wap/menu/student/temp/zzdk/_child_/edit?_t_s_='
        self.headers = {
            'Accept' : 'application/json, text/javascript, */*; q=0.01',
            'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer' : 'http://syxyyqfk.hnsyu.net/index',
            'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
            'X-Requested-With' : 'XMLHttpRequest',
    }
        self.data = {'uname' : uname,'pd_mm' : pd_mm,}
    
    def main(self):
        s = requests.Session()
        r = s.post(self.url, headers=self.headers, data=self.data)
        reg = re.findall(r'(?<=_t_s_=).*(?=",)',r.text)
        token = reg[0]
        logger.info('token: ' + token)
        url_3 = self.url3 + token
        r3 = s.get(url=url_3, headers=self.headers)
        reg1 = re.findall(r'(?<="zzdk_token" value=").*(?=")',r3.text)
        token1 = reg1[0]
        logger.info('token1: ' + token1)
        data1 = {
                'dkdz' : '湖南省永州市中心医院',
                'dkdzZb' : '111.954,26.227',
                'dkly' : 'baidu',
                'zzdk_token': token1,
                'dkd' : '湖南省永州市',
                'jzdValue' : '430000,431100,431103',
                'jzdSheng.dm' : '430000',
                'jzdShi.dm' : '431100',
                'jzdXian.dm' : '431103',
                'jzdDz' : '湖南省永州市中心医院',
                'jzdDz2' : '湖南省永州市中心医院',
                'lxdh' : self.lxdh,
                'sfzx' : '1',
                'sfzx1' : '不在校',
                'twM.dm' : '01',
                'tw1' : '[35.0~37.2]正常',
                'tw1M.dm' : '',
                'tw11' : '',
                'tw2M.dm' : '',
                'tw12' : '',
                'tw3M.dm' : '',
                'tw13' : '',
                'yczk.dm' : '01',
                'yczk1' : '无症状',
                'fbrq' : times,
                'jzInd' : '0',
                'jzYy' : '',
                'zdjg' : '',
                'fxrq' : times,
                'brStzk.dm' : '01',
                'brStzk1' : '身体健康、无异常',
                'brJccry.dm' : '01',
                'brJccry1' : '未接触传染源',
                'jrStzk.dm' : '01',
                'jrStzk1' : '身体健康、无异常',
                'jrJccry.dm' : '01',
                'jrJccry1' : '未接触传染源',
                'jkm' : '1',
                'jkm1' : '绿色',
                'xcm' : '1',
                'xcm1' : '绿色',
                'xgym' : '',
                'xgym1' : '',
                'hsjc' : '',
                'hsjc1' : '',
                'bz' : '实习',
                'operationType' : 'Create',
                'dm' : '',
        }
        url_1 = self.url1 + token
        r1 = s.post(url=url_1,headers=self.headers,data=data1)
        content= r1.text + '\n' + '账号： ' + self.uname + '\n' + '-------------------'
        logger.info(content)
        s.post(url=self.url2, headers=self.headers)
        return content

def run():
    num = 0
    for msg in msgs[0:]:
        signin = SignIn(msg[0],msg[1],msg[2])
        content = signin.main()
        num += 1
        sleep = random.randint(8,16)
        logger.info('随机暂停' + str(sleep) + '秒')
        time.sleep(sleep)
        # if num == 1:
            # push = WxPush()
            # push.push_main(content)
            # requests.get('https://telechan-mu.vercel.app/api/send?sendkey=629979069Tec01f1a418f8781346788d6f468499ec&text=' + content)


if __name__=="__main__":
    run()
