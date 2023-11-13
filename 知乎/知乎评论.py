import hashlib
import re
from base64 import b64encode

import execjs
import requests

cookies = {
    '_zap': 'f21a49dc-ca7a-4f20-b428-312dfaa15103',
    'd_c0': 'AAASj9O4WhePTpsFdIiLTfnBnmAOXm5PQPw=|1694005240',
    'YD00517437729195%3AWM_TID': 'uTaas1NuWBFFRUUUAEOV3GmjkwSy3pF2',
    'YD00517437729195%3AWM_NI': '8fdK8bytEFDD0REa6tgD9rpeChRC3zXwYq9A9OuJu8q7qEyWL6T5Hesc7GPiIqGJCULVkRwCsADOBPciJBYSwOe5yTzppXp0Rjnx81YCCAviBKW1VwrVNVKwdfLoxNPCQkU%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee84e87a8da8a3dab650f8928eb2c44e968e8eacd172a5bef9b3f443f1b6b7dae12af0fea7c3b92afcbaacacbb6abbac8ba7c750f48e8b82b580a59cf793f36f81b89ea4b2729ca99792bc4bfb91bbabf834b3e9bfa6fc5d90ea9cd6cb6fb1bdf9a8d3638baf89abc25f908aa5b3f649b19f8cb0c15ca1b786a3dc59b591abd6fc60bab0c0b9f33c92b6a299bb3b9b9d8da2f563829599d2d57db28a82b7ca7da8ba8490fb46949d9f8cd837e2a3',
    'l_n_c': '1',
    'q_c1': '1b02fe22f189431fa14bcd2314e928e1|1699774834000|1699774834000',
    '_xsrf': 'c72086bae21dbacfec3e216ef9b5206f',
    'r_cap_id': '"NmIxNzFlN2ZkMzVhNDI3Y2I4OWI2ZjZhNzA2ZmVjODA=|1699774834|6149eaa32697581de6cc66c94e45e149f9352c5b"',
    'cap_id': '"YzVkMGU3OWM5ZmQ5NGMxM2FjYjViZmEwYWJjNDVmMzA=|1699774834|1e28edb55b95f8fab48184e914fc174578fde06f"',
    'l_cap_id': '"NjE4MmFlNjRjNGI5NDNhM2FiMWQ0YWQ4MTFkMGE4NmE=|1699774834|180b092af163fbf28630680e65956e662dd8777d"',
    'n_c': '1',
    '__utmc': '51854390',
    '__utmz': '51854390.1699774838.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmv': '51854390.000--|3=entry_date=20231112=1',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1699426413,1699456497,1699519619,1699774868',
    '__utma': '51854390.1425422020.1699774838.1699774838.1699774838.3',
    '__utmb': '51854390.0.10.1699774838',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1699786232',
    'captcha_session_v2': '2|1:0|10:1699786231|18:captcha_session_v2|88:OFV1VDV3bmhPVk5vemI3Ujd0YkF1dVRCMVltcHVsV0NySGhvWGZEMk5VY1pFQWxQYUxtQXFtb3czczBUc3A5aQ==|927663781677db6e8a4d4f1d8a721f973d6ed60b0c55b6033123a0a293707698',
    'KLBRSID': 'd1f07ca9b929274b65d830a00cbd719a|1699786243|1699774834',
}
# td = '101_3_3.0+/api/v4/comment_v5/answers/1514657575/root_comment?order_by=score&limit=20&offset=+"AAASj9O4WhePTpsFdIiLTfnBnmAOXm5PQPw=|1694005240"'

jscode = execjs.compile(open('./参数加密.js', 'r', encoding='utf-8').read()).call('main123')
zse = '2.0_'+ jscode


headers = {
    'authority': 'www.zhihu.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': '_zap=f21a49dc-ca7a-4f20-b428-312dfaa15103; d_c0=AAASj9O4WhePTpsFdIiLTfnBnmAOXm5PQPw=|1694005240; YD00517437729195%3AWM_TID=uTaas1NuWBFFRUUUAEOV3GmjkwSy3pF2; YD00517437729195%3AWM_NI=8fdK8bytEFDD0REa6tgD9rpeChRC3zXwYq9A9OuJu8q7qEyWL6T5Hesc7GPiIqGJCULVkRwCsADOBPciJBYSwOe5yTzppXp0Rjnx81YCCAviBKW1VwrVNVKwdfLoxNPCQkU%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee84e87a8da8a3dab650f8928eb2c44e968e8eacd172a5bef9b3f443f1b6b7dae12af0fea7c3b92afcbaacacbb6abbac8ba7c750f48e8b82b580a59cf793f36f81b89ea4b2729ca99792bc4bfb91bbabf834b3e9bfa6fc5d90ea9cd6cb6fb1bdf9a8d3638baf89abc25f908aa5b3f649b19f8cb0c15ca1b786a3dc59b591abd6fc60bab0c0b9f33c92b6a299bb3b9b9d8da2f563829599d2d57db28a82b7ca7da8ba8490fb46949d9f8cd837e2a3; l_n_c=1; q_c1=1b02fe22f189431fa14bcd2314e928e1|1699774834000|1699774834000; _xsrf=c72086bae21dbacfec3e216ef9b5206f; r_cap_id="NmIxNzFlN2ZkMzVhNDI3Y2I4OWI2ZjZhNzA2ZmVjODA=|1699774834|6149eaa32697581de6cc66c94e45e149f9352c5b"; cap_id="YzVkMGU3OWM5ZmQ5NGMxM2FjYjViZmEwYWJjNDVmMzA=|1699774834|1e28edb55b95f8fab48184e914fc174578fde06f"; l_cap_id="NjE4MmFlNjRjNGI5NDNhM2FiMWQ0YWQ4MTFkMGE4NmE=|1699774834|180b092af163fbf28630680e65956e662dd8777d"; n_c=1; __utmc=51854390; __utmz=51854390.1699774838.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|3=entry_date=20231112=1; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1699426413,1699456497,1699519619,1699774868; __utma=51854390.1425422020.1699774838.1699774838.1699774838.3; __utmb=51854390.0.10.1699774838; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1699786232; captcha_session_v2=2|1:0|10:1699786231|18:captcha_session_v2|88:OFV1VDV3bmhPVk5vemI3Ujd0YkF1dVRCMVltcHVsV0NySGhvWGZEMk5VY1pFQWxQYUxtQXFtb3czczBUc3A5aQ==|927663781677db6e8a4d4f1d8a721f973d6ed60b0c55b6033123a0a293707698; KLBRSID=d1f07ca9b929274b65d830a00cbd719a|1699786243|1699774834',
    'pragma': 'no-cache',
    'referer': 'https://www.zhihu.com/topic/19555513/hot',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': zse,
}

params = {
    'order_by': 'score',
    'limit': '20',
    'offset': '0_727607312_0',
}

response = requests.get(
    'https://www.zhihu.com/api/v4/comment_v5/articles/80292665/root_comment',
    params=params,
    cookies=cookies,
    headers=headers,
).json()
# print(response)
# next = response['paging']['next']
# # print(next)
# next_page = re.findall(r'limit=10&offset=(.*?)&order', next)[0]
# print(next_page)
list = response['data']
for datas in list:
    content = datas['content']
    like_count = datas['like_count'] #点赞
    author = datas['author']['name']
    child_comment = datas['child_comments']
    print("评论:",content,"点赞量:", like_count,"用户名:", author,)
    for comment in child_comment:
        reply = comment['content']
        print("回复:",reply)
    print("=============================================")

