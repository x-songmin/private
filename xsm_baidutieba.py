# -*- coding: utf8 -*-
from requests import Session
from time import sleep

'''
cron:  40 8 * * *
new Env('xsm_贴吧');
'''
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)
def main(*args):
    # 数据134
    like_url = 'https://tieba.baidu.com/mo/q/newmoindex?'
    sign_url = 'http://tieba.baidu.com/sign/add'
    tbs = '4fb45fea4498360d1547435295'
    head = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'BAIDUID=2F3F5879FC3146338749C7D0FDDA6CEE:FG=1; bdshare_firstime=1600785423740; BAIDUID_BFESS=11BDF5F2EDB8C89D95EFFB22DBB53207:FG=1; BIDUPSID=2F3F5879FC3146338749C7D0FDDA6CEE; PSTM=1605971578; __yjs_duid=1_f20948debf2b1b0c6631ef74ad5782741610704190790; BDUSS=RLdUdoem9MNlFZLWI5RWNXSUxNUWtJTDQ5YzRVWDR3RDM1OGVhc0Y3aUVTVEpnRVFBQUFBJCQAAAAAAAAAAAEAAAAMqK5yz8TaoefkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIS8CmCEvApgMG; BDUSS_BFESS=RLdUdoem9MNlFZLWI5RWNXSUxNUWtJTDQ5YzRVWDR3RDM1OGVhc0Y3aUVTVEpnRVFBQUFBJCQAAAAAAAAAAAEAAAAMqK5yz8TaoefkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIS8CmCEvApgMG; STOKEN=51b1a196bd5dc3a5d6b86571617f638f5c8fa80a2e1d54df39869475f9d0b4bf; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1612184275; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1612184275; ab_sr=1.0.0_ZTAwOGUzYTZlN2Q5Mjg4NDk4MzA1ZDZjNmU2YzA2YjQ0NmZhMjQxOGYwZGU4Mzc4NTIwZmVlOTE2NmVkMjI0NGM0MDE1NTMwYTRkZDQxODEwNDI2YTljYzJmYjY2ZjRjMzM4NDA0YTY2N2FkZmVmYTBiYjEyZGE5NGUzYzU3ZGI=; st_data=1f180e88b13de7f68443d9a2234d55b1581415e6d8174e5721781d13cca3e3842c4461141a96cef0509a3b1daaee06e7756c8bbb9a71a4256cd8df9a73f422b487cb885f29f58063c5f475b4fb33692d7de853ef9aeab69c8ee823de8318a2fcf497323966677b126661b7e157879df718de04fe0a253df319302d6c3862d87e; st_key_id=17; st_sign=ab686c18',  #这里填写cookice  这里填写cookice   这里填写cookice
        'Host': 'tieba.baidu.com',
        'Referer': 'http://tieba.baidu.com/i/i/forum',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
    s = Session()
 
 
    # 获取关注的贴吧
    bars = []
    dic = s.get(like_url, headers=head).json()['data']['like_forum']
    for bar_info in dic:
        bars.append(bar_info['forum_name'])
 
 
    # 签到
    already_signed_code = 1101
    success_code = 0
    need_verify_code = 2150040
    already_signed = 0
    succees = 0
    failed_bar = []  #失败列表
    n = 0
    retry_count = 0
    max_retry = 5 
 
    while n < len(bars):
        sleep(0.5)
        bar = bars[n]
        data = {
            'ie': 'utf-8',
            'kw': bar,
            'tbs': tbs
        }
        try:
            r = s.post(sign_url, data=data, headers=head)
        except Exception as e:
            logger.info(f'未能签到{bar}, 由于{e}。')
            failed_bar.append(bar)
            continue
        dic = r.json()
        msg = dic['no']
        if msg == already_signed_code: already_signed += 1; r = '已经签到过了!'
        elif msg == need_verify_code and retry_count <max_retry: n -= 1; retry_count += 1; r = f'需要验证码，即将重试!({retry_count}/{max_retry})'
        elif msg == need_verify_code: r = '验证码错误，跳过！'; retry_count = 0
        elif msg == success_code: r = f"签到成功!你是第{dic['data']['uinfo']['user_sign_rank']}个签到的吧友,共签到{dic['data']['uinfo']['total_sign_num']}天。"
        else: r = '未知错误!' + dic['error']
        logger.info(f"{bar}：{r}")
        succees += 1
        n += 1
    l = len(bars)
    failed = "\n失败列表："+'\n'.join(failed_bar) if len(failed_bar) else ''
    message = f'''百度贴吧: 共{l}个吧，其中{succees}个吧签到成功，{len(failed_bar)}个吧签到失败，{already_signed}个吧已经签到。失败列表：{failed}'''
    logger.info(message)      #下一行修改Server酱推送  下一行修改Server酱推送   下一行修改Server酱推送
   # s.get(f"https://sctapi.ftqq.com/SCT1450TJ4BtzkQZuaGEGzGAhYtFmquM.send?text={message}")# [未测试]Server酱推送，不需要则删除此行
    # s.get(f"https://push.xuthus.cc/send/04d949bd3fcbca88?c={message}")   #修改qqt通知   修改qqt通知   修改qqt通知
    s.get(f'https://sc.ftqq.com/SCU109954T1eec53fd29a2455979eb5183afe09ba35f3cc08d82b94.send?text={message}')

if __name__ == '__main__':
    main()
def main_handler(event, context):
    main()
