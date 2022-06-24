import requests,os,logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

content = os.getenv('content')

class WxPush():
    def __init__(self):
        self.corpid = 'ww7aa45d1915be80d0'  # 企业id
        self.agentid = 1000003  # 应用ID
        self.corpsecret = 'zov0_wqraq8--BWhSoPwYw0G9KViMqH2rw9TNqOHg4w'  # 应用密钥
        self.mbr = 'XiaSongmin'  # 成员ID，默认@all,MeiYouNiCheng

    def push_main(self,content):
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + self.corpid + '&corpsecret=' + self.corpsecret).json()
        access_token = r['access_token']
        # print(access_token)
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
        logger.info(requests.post(url=url, json=json))



if __name__=="__main__":
    # content = input("输入推送文本：")
    push = WxPush()
    push.push_main(content)
