import requests,time,re,logging,random

'''
cron:  30 6 * * *
new Env('xsm_疫情打卡测试');
'''

#日志输出
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# data时间参数
time = time.strftime('%Y-%m-%d')

# 登录数据
url = 'http://syxyyqfk.hnsyu.net/website/login'
headers = {
        'Accept' : 'application/json, text/javascript, */*; q=0.01',
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer' : 'http://syxyyqfk.hnsyu.net/index',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
        'X-Requested-With' : 'XMLHttpRequest',
}


msgs = (
    ['1841601149','9b28aa558cb112969fc62a18d08f143a','17674534215'],
    ['1841601143','19830a9035b408c82a626c10db060c26','18573620025'],
    ['1841601116','6ecbea51bcb83c31176edbc426f34f80','18707395377'],
    ['1841601125','2acaaa04abb5ed1d32e975779b9f8f91','17761149807'],
    ['1841601117','ac2dba197eb6b38c61caa84143b3eda0','15115986876'],
    ['1841601133','fab28aead6b3c8349023bd8fbefda54e','13562943296'],
)

class SignIn():
    def start(self,uname,pd_mm,lxdh):
        data = {'uname' : uname,'pd_mm' : pd_mm,}
        data1 = {
            'dkdz' : '湖南省邵阳市大祥区城北路6号',
            'dkdzZb' : '111.468,27.239',
            'dkly' : 'baidu',
            'dkd' : '湖南省邵阳市',
            'jzdValue' : '430000,430500,430503',
            'jzdSheng.dm' : '430000',
            'jzdShi.dm' : '430500',
            'jzdXian.dm' : '430503',
            'jzdDz' : '邵阳学院西湖校区',
            'jzdDz2' : '1#305',
            'lxdh' : lxdh,
            'sfzx' : '1',
            'sfzx1' : '在校',
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
            'fbrq' : time,
            'jzInd' : '0',
            'jzYy' : '',
            'zdjg' : '',
            'fxrq' : time,
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
            'bz' : '',
            'operationType' : 'Create',
            'dm' : '',
    }

        s = requests.Session()
        r = s.post(url, headers=headers, data=data)

        reg = re.findall(r'(?<=_t_s_=).*(?=",)',r.text)

        token = reg[0]
        logger.info(token)
        url1 = 'http://syxyyqfk.hnsyu.net/content/student/temp/zzdk?_t_s_=' + token
        r1 = s.post(url=url1,headers=headers,data=data1)

        print(r1.text + uname + '\n' + '---------------')
        # logger.info(r1.text)
        # requests.get('https://telechan-mu.vercel.app/api/send?sendkey=629979069Tec01f1a418f8781346788d6f468499ec&text=' + r1.text)
        s.post(url='http://syxyyqfk.hnsyu.net/website/logout',headers=headers)

for msg in msgs[0:] :
    signin = SignIn()
    signin.start(msg[0],msg[1],msg[2])
    sleep = random.randint(5,11)

