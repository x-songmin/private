import requests,time,random,logging

'''
cron:  20 6 * * * oppo_community.py
new Env('oppo社区');
'''

logger = logging.getLogger()
cookies = [';token=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2NDA3NjMxNTgwNDcsImlkIjoiNDgyMzU1MTMyIiwiaWRjIjoic2hvdW1pbmciLCJ0aWQiOiJUZ2FDZWVlR1hxdjFINkdFc0RmaVdjeEdiZys2R1hJNkJNdmJFbnhKZU5yTnNQVFZYMnMxZlMrZHRabmlMcGY4a0RGVlo0Z1VkblNJWGw3NzZ6eGdzeGh6UUZNZkFwbEh4aU5hZkV3bDVYYz0ifQ.MEUCICF5ifQhCo9o-zfSkBAuvjaEnPjZ34JPzRQgWlOVfqHGAiEAsncvZujPEzd9CbHCSkZ9Ch-4aoqD-AxA0i7sdRFbnWk',';token=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2NDA3NDM4MDA0NDQsImlkIjoiNjcwODE4MTQxIiwiaWRjIjoic2hvdW1pbmciLCJ0aWQiOiJNVkE2b2FJNS83OGluS3FCb2c2VGd3ZG1jUkhMM3lHWDArazk3UGpOd0VhSlhJVE1naUFGMGVlaDlmVEJqUkxabWN4ZmJYajBCbjlrMlVqcUhGNllUTGd3dDUyQ1Vvb29ZMENRWE1CU251az0ifQ.MEUCIQCglXpJbK54M1XYxrkoAN3TuD_5Fl6fDnczlVgzRvzZIAIgDII_V9rjyZw1QzhMvGgWUPX1RN-tX8-Cs9xJPF87SEM',';token=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2NDA3NDM1NDEyMDIsImlkIjoiNjg4Njg5MTUzIiwiaWRjIjoic2hvdW1pbmciLCJ0aWQiOiJRY0RsWng0L0taR0dMNm1JSnhuaDR3ZG1jUkhMM3lHWDArazk3UGpOd0VhSlhJVE1naUFGMGVlaDlmVEJqUkxacXJGMGdrS2FnekpUWjNpUkc0bXptRlVOelN1WEdOVW5Pei9yV2M0cVB0bz0ifQ.MEUCIFp40ynV7FU48XsJXoeeTTVqUXSbqO_IRkzVLRPDy-SvAiEAmQ8aSTWhqvQEeOsVYFOF-6mERVIcz5IZqOon1_WPX4M',';token=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2NDA3NDM2ODM1MDksImlkIjoiMTAxNDcyMTM2IiwiaWRjIjoic2hvdW1pbmciLCJ0aWQiOiIrK2ZRWWw5RTBveTdyanorMlJQVDdRZG1jUkhMM3lHWDArazk3UGpOd0VhSlhJVE1naUFGMGVlaDlmVEJqUkxaRXVKSk41VHkwbENKbWxZSENDa01adTRxMjFIZ2d2ZDZyS0t5bzVpaFJZdz0ifQ.MEYCIQD9zHMbJsq5V67vRwlrD9epTKmsOwTQj_3Ag5sJCLlYRwIhAPObTdMPYNW3IsPOVUTmIoc5eAuUJrL65M-t9uKgU6A6']

# # 任务提交
# url = 'https://i-api.oppo.cn/java/task/api/browse/browseFinish'
# headers = {
#         'cookie': cookie,
#         'globalRequest': 'eyJwbGF0Zm9ybSI6ImFuZHJvaWQiLCJ1YSI6Im9wcG9jb21tdW5pdHkiLCJtb2RhbCI6IkdNMTkxMCIsInVzZV9za2luIjoiZmFsc2UiLCJzY3JlZW5fc2l6ZSI6IjE0NDB4MzEyMCIsIm9zIjoiMTEiLCJjb2xvcl9vcyI6IjAiLCJzX3ZlcnNpb24iOiI4MTIwMiIsImltZWkiOiJYMSt4OGNmelJCRHg1U1Vxd2E2Nkx5VnV5Qk1sNjhGS0xNZTlSV1FpSzFRPSIsIm5ldHdvcmt0eXBlIjoid2lmaSIsInZhaWQiOiI1NjBEQTVEOTYwMEE0RTM0OTgzRjVGOEY0OERGRjRFMEVDN0Q0MjQ5NzlDQzlDNTEyOThEQkU5NzE0N0IzNUQwIiwib2FpZCI6IkExQUM1NjExNzhEREQ4NkY0MzAwM0MzQzQ5RjBDOTBCNkIwMjc1MzdCRkQyRjVBQjgyMDMwNzE2NDNCNDI1OTQiLCJ1ZGlkIjoiIiwiYWFpZCI6IiIsInV1aWQiOiJhMzU5OWI4Yy05OGJjLTQ2MTEtODhhOS0zMzlkMTZiYzM0YTIiLCJjb2xvcl9vc19uYW1lIjoibnVsbCJ9',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Content-Length': '76',
#         'Host': 'i-api.oppo.cn',
#         'Connection': 'Keep-Alive',
#         'Accept-Encoding': 'gzip',
#         'User-Agent': 'okhttp/3.12.12.217',
#         'TAP-GSLB': '0,0',
#         'Route-Data': 'MQE0NTY0NwEyLjEyLjIBR00xOTEwAU9uZVBsdXMBQ04B',
# }

# data = {
#         'systemId':'520',
#         '_t':'1638257603479',
#         '_sign':'8af564588a935ce6c31227049818eb6f56a58f89',
# }

# for i in range(1,11):
#     re = requests.post(url=url,headers=headers,data=data)
#     logger.infot('第' + str(i) +'次')
#     print('第' + str(i) +'次')
#     i +=1
#     time.sleep(random.randint(2,5))
# # 奖励领取提交
# headers1 = {
# 'Host' : 'www.oppo.cn',
# 'Connection' : 'keep-alive',
# 'Content-Length' : '10',
# 'Pragma' : 'no-cache',
# 'Cache-Control' : 'no-cache',
# 'User-Agent' : 'Mozilla/5.0 (Linux; Android 11; GM1910 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 oppocommunity/0_4f0892b_210810',
# 'X-Requested-With' : 'XMLHttpRequest',
# 'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8',
# 'Accept' : '*/*',
# 'Origin' : 'https//hybrid.oppo.cn',
# 'Sec-Fetch-Site' : 'same-site',
# 'Sec-Fetch-Mode' : 'cors',
# 'Sec-Fetch-Dest' : 'empty',
# 'Referer' : 'https//hybrid.oppo.cn/',
# 'Accept-Encoding' : 'gzip, deflate',
# 'Accept-Language' : 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
# 'Cookie' : '_ga=GA1.2.284397977.1633261411; dcs-uuid=1719e230-2525-440b-8536-9918ba4711e1; _gid=GA1.2.2107911929.1638257519' +  cookie + '; _gat_gtag_UA_29338249_8=1',
# }
# data1 = {'idList':'520'}
# url1 = "https://www.oppo.cn/java/task/api/browse/awardBrowseTask"

# re1 = requests.post(url=url1,headers=headers1,data=data1)
# logger.info(re1.text)
# print(re1.text)





n = 1

for cookie in cookies[0:]:
    url = 'https://i-api.oppo.cn/java/task/api/browse/browseFinish'
    headers = {
        'cookie': cookie,
        'globalRequest': 'eyJwbGF0Zm9ybSI6ImFuZHJvaWQiLCJ1YSI6Im9wcG9jb21tdW5pdHkiLCJtb2RhbCI6IkdNMTkxMCIsInVzZV9za2luIjoiZmFsc2UiLCJzY3JlZW5fc2l6ZSI6IjE0NDB4MzEyMCIsIm9zIjoiMTEiLCJjb2xvcl9vcyI6IjAiLCJzX3ZlcnNpb24iOiI4MTIwMiIsImltZWkiOiJYMSt4OGNmelJCRHg1U1Vxd2E2Nkx5VnV5Qk1sNjhGS0xNZTlSV1FpSzFRPSIsIm5ldHdvcmt0eXBlIjoid2lmaSIsInZhaWQiOiI1NjBEQTVEOTYwMEE0RTM0OTgzRjVGOEY0OERGRjRFMEVDN0Q0MjQ5NzlDQzlDNTEyOThEQkU5NzE0N0IzNUQwIiwib2FpZCI6IkExQUM1NjExNzhEREQ4NkY0MzAwM0MzQzQ5RjBDOTBCNkIwMjc1MzdCRkQyRjVBQjgyMDMwNzE2NDNCNDI1OTQiLCJ1ZGlkIjoiIiwiYWFpZCI6IiIsInV1aWQiOiJhMzU5OWI4Yy05OGJjLTQ2MTEtODhhOS0zMzlkMTZiYzM0YTIiLCJjb2xvcl9vc19uYW1lIjoibnVsbCJ9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '76',
        'Host': 'i-api.oppo.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.12.217',
        'TAP-GSLB': '0,0',
        'Route-Data': 'MQE0NTY0NwEyLjEyLjIBR00xOTEwAU9uZVBsdXMBQ04B',
}

    data = {
        'systemId':'520',
        '_t':'1638257603479',
        '_sign':'8af564588a935ce6c31227049818eb6f56a58f89',
}
    headers1 = {
    'Host' : 'www.oppo.cn',
    'Connection' : 'keep-alive',
    'Content-Length' : '10',
    'Pragma' : 'no-cache',
    'Cache-Control' : 'no-cache',
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 11; GM1910 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 oppocommunity/0_4f0892b_210810',
    'X-Requested-With' : 'XMLHttpRequest',
    'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8',
    'Accept' : '*/*',
    'Origin' : 'https//hybrid.oppo.cn',
    'Sec-Fetch-Site' : 'same-site',
    'Sec-Fetch-Mode' : 'cors',
    'Sec-Fetch-Dest' : 'empty',
    'Referer' : 'https//hybrid.oppo.cn/',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie' : '_ga=GA1.2.284397977.1633261411; dcs-uuid=1719e230-2525-440b-8536-9918ba4711e1; _gid=GA1.2.2107911929.1638257519' +  cookie + '; _gat_gtag_UA_29338249_8=1',
    }
    data1 = {'idList':'520'}
    url1 = "https://www.oppo.cn/java/task/api/browse/awardBrowseTask"

    for i in range(1,11):
        re = requests.post(url=url,headers=headers,data=data)
        logger.info('第' + str(i) +'次')
        print('第' + str(i) +'次')
        i +=1
        time.sleep(random.randint(2,5))

    re1 = requests.post(url=url1,headers=headers1,data=data1)
    logger.info(re1.text)
    print(re1.text)

    print('第' + str(n) + '个号')
    n +=1
