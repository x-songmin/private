import requests,time,re,logging

'''
cron:  30 6 * * *
new Env('xsm_疫情打卡');
'''

#日志输出
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# 登录
url = 'http://syxyyqfk.hnsyu.net/website/login'
headers = {
        'Accept' : 'application/json, text/javascript, */*; q=0.01',
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer' : 'http://syxyyqfk.hnsyu.net/index',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
        'X-Requested-With' : 'XMLHttpRequest',
}
data = {'uname' : '1841601149','pd_mm' : '9b28aa558cb112969fc62a18d08f143a',}

# 提交

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
'lxdh' : '17674534215',
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
'fbrq' : '2022-04-23',
'jzInd' : '0',
'jzYy' : '',
'zdjg' : '',
'fxrq' : '2022-04-23',
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

print = r1.text
logger.info(r1.text)
