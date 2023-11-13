import time

import execjs
import requests



cookies = {
    'UOR': 'cn.bing.com,tousu.sina.com.cn,',
    'SINAGLOBAL': '223.104.25.245_1699449383.317126',
    'Apache': '223.104.25.245_1699449383.317127',
    'ULOGIN_IMG': 'yf-b891945fb7da818efe1255c77237c7cc93f8',
    'ULV': '1699449410750:2:2:2:223.104.25.245_1699449383.317127:1699449384092',
    'SUB': '_2A25IT_oKDeRhGeBG41YQ8CjOzzuIHXVrJXPCrDV_PUNbm9ANLWjAkW9NQfksaWu-572WGgxDWVfjFRnzknIWvj4i',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhTXueU27FTXWWrV-TbTRAK5JpX5KzhUgL.FoqR1hBpehqEShM2dJLoIpjLxKqL1KMLBKMLxKqL1KMLBoqLxK-L1h.L1K2t',
    'ALF': '1702041434',
    'U_TRS1': '000000f5.e59a27185.654b8a5a.9f361d04',
    'U_TRS2': '000000f5.e5a527185.654b8a5a.82632ca4',
}

headers = {
    'authority': 'tousu.sina.com.cn',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'UOR=cn.bing.com,tousu.sina.com.cn,; SINAGLOBAL=223.104.25.245_1699449383.317126; Apache=223.104.25.245_1699449383.317127; ULOGIN_IMG=yf-b891945fb7da818efe1255c77237c7cc93f8; ULV=1699449410750:2:2:2:223.104.25.245_1699449383.317127:1699449384092; SUB=_2A25IT_oKDeRhGeBG41YQ8CjOzzuIHXVrJXPCrDV_PUNbm9ANLWjAkW9NQfksaWu-572WGgxDWVfjFRnzknIWvj4i; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhTXueU27FTXWWrV-TbTRAK5JpX5KzhUgL.FoqR1hBpehqEShM2dJLoIpjLxKqL1KMLBKMLxKqL1KMLBoqLxK-L1h.L1K2t; ALF=1702041434; U_TRS1=000000f5.e59a27185.654b8a5a.9f361d04; U_TRS2=000000f5.e5a527185.654b8a5a.82632ca4',
    'pragma': 'no-cache',
    'referer': 'https://tousu.sina.com.cn/index/search/?keywords=%E7%AF%AE%E7%90%83&t=1',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}




for page in range(1,10):
    keyword = '中公教育'
    timestamp = str(round(time.time() * 1000))
    print(timestamp)
    sign = execjs.compile(open('参数加密hmts.js', 'r', encoding='utf-8').read()).call('abc', timestamp,keyword)
    print(sign)
    rs = sign['p']
    signature = sign['sign']
    time1 = sign['timestamp']
    params = {
        'ts': time1,
        'rs': rs,
        'signature': signature,
        'keywords': keyword,
        'page_size': '10',
        'page': page,
    }
    print(params)
    print('第{page}页'.format(page=page))
    time.sleep(1)
    response = requests.get('https://tousu.sina.com.cn/api/index/s', params=params, cookies=cookies, headers=headers).json()
    print(response)
    # lists = response['result']['data']['lists']
    # for list in lists:
    #     title = list['main']['title'].replace('<span class="code-red">','').replace('</span>','')
    #     summary = list['main']['summary']
    #     print('投诉标题:',title)
    #     print('投诉内容:',summary)