import json

import execjs
import requests
from datetime import datetime

# 获取当前时间
current_time = datetime.now()

# 将当前时间转换为精确到毫秒的时间戳
timestamp = int(current_time.timestamp() * 1000)

# print(timestamp)
cookies = {
    'miid': '658036801754566009',
    'thw': 'cn',
    't': '82127e0c71c79c2739bfa6f124d16e34',
    '_tb_token_': '83ee13571413',
    'cna': 'qniFHSKv72UCAbdFjZ3Q2caY',
    '_m_h5_tk': '36bd5d00891d801e601de423e5d7905c_1699691354976',
    '_m_h5_tk_enc': '110c0cec396bcc4525200182402ac5a6',
    'xlly_s': '1',
    'cookie2': '1f7ca8b883dec43bad2f3249dd7597be',
    '_samesite_flag_': 'true',
    'sgcookie': 'E100EeX2ExCs2NUHwtrA1o2K2X0xrQBizQDq4zKli7ffIa%2FZ3%2Fpb82P4b6eU2xV4MWTbdAky08byBWBKaPvWpJ0YEyfKmqHrY8Cp7kI4jfDB1cQ%3D',
    'unb': '3326796581',
    'uc3': 'lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD3CIZ0wj%2FYvJm7X8%3D&id2=UNN%2F6l3Nkrtvdg%3D%3D&nk2=yxAOtfINVEKxE0TbrnipSn%2F2',
    'csg': 'ff52b51f',
    'lgc': '%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4',
    'cancelledSubSites': 'empty',
    'cookie17': 'UNN%2F6l3Nkrtvdg%3D%3D',
    'dnk': '%5Cu8096%5Cu5947%5Cu4F26xqlun',
    'skt': 'c9b308687e46db68',
    'existShop': 'MTY5OTY4MjE3Mg%3D%3D',
    'uc4': 'id4=0%40UgQ3BdKawHgAB9Z7r%2Fn%2BrcjXhKgy&nk4=0%40ySlAcaTuheswgUPc6Shw%2B3KBWONUU1nWuDFvXDM%3D',
    'tracknick': '%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4',
    '_cc_': 'UIHiLt3xSw%3D%3D',
    '_l_g_': 'Ug%3D%3D',
    'sg': '%E5%B7%B41d',
    '_nk_': '%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4',
    'cookie1': 'Vy0Vzmb8naRYzvJNN1XCN55Q5E1L1SO7ceqWi63rb1I%3D',
    'uc1': 'cookie21=VFC%2FuZ9aiKIc&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&cookie14=Uoe9ZL5VeF44eQ%3D%3D&pas=0&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D',
    'tfstk': 'dQaBJEXBcpvIYPnJ8w1aCKEKsKg7AJ_q9QG8i7Lew23d2YMaw6VUTMb7fS2SL_jn8lM7BRMpL28UC7eZIzrFZMYRNSDiUyuKe0OtZ-53F7fnwYe8FYrFbZP3t40R34_VuWqJb9CqXO5mB2bsytWVuhRtx9u8Yvx5uGYJM_b957B6WFTVlKeRb1ZUxPGIXGPKB-yRaXmCz5kMyTnNQtYqhpUMVCiDPfMV11tkqlME_UC..',
    'l': 'fBjZ-zFuPs5O3hIjBO5Bhurza77tFQObzoVzaNbMiIEGa6Gf6Gy9yNCTt81BJdtjgT5mTetrWDM-1dek-54U-EODshcjMWPhcC9eReM3N7AN.',
    'isg': 'BOvruP0MCn1zRFapW1SDjQQfeg_VAP-CPAHA0F1r4Sth_Ale5dGn0yQaVjySWFd6',
}

headers = {
    'authority': 'h5api.m.taobao.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'miid=658036801754566009; thw=cn; t=82127e0c71c79c2739bfa6f124d16e34; _tb_token_=83ee13571413; cna=qniFHSKv72UCAbdFjZ3Q2caY; _m_h5_tk=36bd5d00891d801e601de423e5d7905c_1699691354976; _m_h5_tk_enc=110c0cec396bcc4525200182402ac5a6; xlly_s=1; cookie2=1f7ca8b883dec43bad2f3249dd7597be; _samesite_flag_=true; sgcookie=E100EeX2ExCs2NUHwtrA1o2K2X0xrQBizQDq4zKli7ffIa%2FZ3%2Fpb82P4b6eU2xV4MWTbdAky08byBWBKaPvWpJ0YEyfKmqHrY8Cp7kI4jfDB1cQ%3D; unb=3326796581; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD3CIZ0wj%2FYvJm7X8%3D&id2=UNN%2F6l3Nkrtvdg%3D%3D&nk2=yxAOtfINVEKxE0TbrnipSn%2F2; csg=ff52b51f; lgc=%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4; cancelledSubSites=empty; cookie17=UNN%2F6l3Nkrtvdg%3D%3D; dnk=%5Cu8096%5Cu5947%5Cu4F26xqlun; skt=c9b308687e46db68; existShop=MTY5OTY4MjE3Mg%3D%3D; uc4=id4=0%40UgQ3BdKawHgAB9Z7r%2Fn%2BrcjXhKgy&nk4=0%40ySlAcaTuheswgUPc6Shw%2B3KBWONUU1nWuDFvXDM%3D; tracknick=%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%B7%B41d; _nk_=%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4; cookie1=Vy0Vzmb8naRYzvJNN1XCN55Q5E1L1SO7ceqWi63rb1I%3D; uc1=cookie21=VFC%2FuZ9aiKIc&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&cookie14=Uoe9ZL5VeF44eQ%3D%3D&pas=0&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D; tfstk=dQaBJEXBcpvIYPnJ8w1aCKEKsKg7AJ_q9QG8i7Lew23d2YMaw6VUTMb7fS2SL_jn8lM7BRMpL28UC7eZIzrFZMYRNSDiUyuKe0OtZ-53F7fnwYe8FYrFbZP3t40R34_VuWqJb9CqXO5mB2bsytWVuhRtx9u8Yvx5uGYJM_b957B6WFTVlKeRb1ZUxPGIXGPKB-yRaXmCz5kMyTnNQtYqhpUMVCiDPfMV11tkqlME_UC..; l=fBjZ-zFuPs5O3hIjBO5Bhurza77tFQObzoVzaNbMiIEGa6Gf6Gy9yNCTt81BJdtjgT5mTetrWDM-1dek-54U-EODshcjMWPhcC9eReM3N7AN.; isg=BOvruP0MCn1zRFapW1SDjQQfeg_VAP-CPAHA0F1r4Sth_Ale5dGn0yQaVjySWFd6',
    'origin': 'https://zc-paimai.taobao.com',
    'pragma': 'no-cache',
    'referer': 'https://zc-paimai.taobao.com/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}
for page in range(1, 6):
    data = {
        'data': '{"dfApp":"auctionwalle","dfApiName":"auctionwalle.datou.getPageModulesData","dfVariables":"{\\"pageId\\":1410667,\\"moduleIds\\":\\"9018433170:items\\",\\"context\\":{\\"_b_9018433170:items\\":\\"{\\\\\\"spm\\\\\\":\\\\\\"a2129.27064540.puimod-zc-focus-2021_2860107850.category-1-1\\\\\\",\\\\\\"pmid\\\\\\":\\\\\\"0406242018_1699682775662\\\\\\",\\\\\\"pmtk\\\\\\":\\\\\\"20140647.0.0.0.27064540.puimod-zc-focus-2021_2860107850.category-1-1\\\\\\",\\\\\\"path\\\\\\":\\\\\\"27064540\\\\\\",\\\\\\"scm\\\\\\":\\\\\\"20140647.julang.360_search.brand\\\\\\",\\\\\\"userInfo\\\\\\":{\\\\\\"userId\\\\\\":\\\\\\"3326796581\\\\\\"},\\\\\\"page\\\\\\":\\\\\\"%d\\\\\\",\\\\\\"appendMap\\\\\\":{\\\\\\"sid\\\\\\":\\\\\\"3366366005_1699682797554\\\\\\"}}\\",\\"userInfo\\":\\"{}\\",\\"device\\":\\"pc\\",\\"sceneCode\\":\\"20200713C5R32B6N\\"}}","dfUniqueId":"1410667.9018433170:items","dfVariablesRecover":"{}"}' % page,
    }

    data1 = data['data']
    jscode = execjs.compile(open('./参数加密.js', 'r', encoding='utf-8').read()).call('main123', data1, timestamp)

    params = {
        'jsv': '2.6.1',
        'appKey': '12574478',
        't': timestamp,
        'sign': jscode,
        'bxPageId': '1410667',
        'api': 'mtop.taobao.datafront.invoke.auctionwalle',
        'v': '1.0',
        'type': 'originaljson',
        'dataType': 'json',
        'requiredParams': 'dfApiName,dfUniqueId',
    }


    response = requests.post(
        'https://h5api.m.taobao.com/h5/mtop.taobao.datafront.invoke.auctionwalle/1.0/',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    ).json()
    print(response)