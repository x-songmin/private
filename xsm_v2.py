import requests
'''
cron:  20 8 * * *
new Env('xsm_v2ray');
'''
# sckey = 'SCU109954T1eec53fd29a2455979eb5183afe09ba35f3cc08d82b94'
url = 'https://cv2.dog/auth/login'
url1 = 'https://cv2.dog//user/checkin'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://cv2.dog/auth/login',
    'origin': 'https://cv2.dog'
}
headers1 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://cv2.dog/user',
    'origin': 'https://cv2.dog'
}
data = {
    'email': 'wsjyfm@gmail.com',
    'passwd': 'wsjyfm@gmail.com',
    'code': ''
}
def run():
    s = requests.Session()
    r = s.post(url, headers=headers, data=data)
    value = r.text    # print(value)   # 成功{"ret":1,"msg":"\u767b\u5f55\u6210\u529f"}   失败{"ret":0,"msg":"\u90ae\u7bb1\u6216\u8005\u5bc6\u7801\u9519\u8bef"}
    value_1 = eval(value)     # print(type(value))   eval把字符串转化为字典,value是str,value_1是dic
    print(value_1)
    num1 = value_1['msg']    # print(type(value_1))   # print(value_1['ret'])

    value_end = value_1['ret']
    if value_end == 1:
        print('登录成功')
        r1 = s.post(url1, headers=headers1)
        print(eval(r1.text))
        value_2 = eval(r1.text)
        num2 = value_2['msg']
        # requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + num1 + ':' + num2 + '&desp=' + num2)
    else:
        print('登录失败')
        # requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + num1 + '&desp=登陆失败')


if __name__=="__main__":
    run()

def main_handler(event, context):
    run()


