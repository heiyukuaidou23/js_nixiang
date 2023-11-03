import json

import requests
import execjs

cookies = {
    'locale': 'zh_CN',
    'browserVersionLevel': 'v5.8e6ec7b1e6dc',
    'devId': 'bb80219f-5b5d-421b-b47b-e1867a714e90',
    'aliyungf_tc': 'cc0eeb5aaa37faae1040e981362075a7e6c6445cbfc1de04ca2e363252653cf2',
    '_monitor_extras': '{"deviceId":"vI6YPFfbhXMCrfLYtZyKBB","eventId":34,"sequenceNumber":34}',
    'amp_d77757': 'p3bhakR5C5yZ1bp_Rcc3-o...1he9us844.1he9ut67v.11.0.11',
    'okg.currentMedia': 'sm',
}

js_code = execjs.compile(open('btc_.js', 'r', encoding='utf-8').read()).call('getApiKey')
print(js_code)
headers = {
    'authority': 'www.oklink.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'app-type': 'web',
    'cache-control': 'no-cache',
    # 'cookie': 'locale=zh_CN; browserVersionLevel=v5.8e6ec7b1e6dc; devId=bb80219f-5b5d-421b-b47b-e1867a714e90; aliyungf_tc=cc0eeb5aaa37faae1040e981362075a7e6c6445cbfc1de04ca2e363252653cf2; _monitor_extras={"deviceId":"vI6YPFfbhXMCrfLYtZyKBB","eventId":34,"sequenceNumber":34}; amp_d77757=p3bhakR5C5yZ1bp_Rcc3-o...1he9us844.1he9ut67v.11.0.11; okg.currentMedia=sm',
    'devid': 'bb80219f-5b5d-421b-b47b-e1867a714e90',
    'pragma': 'no-cache',
    'referer': 'https://www.oklink.com/cn/btc/tx-list',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'x-apikey': js_code,
    'x-cdn': 'https://static.oklink.com',
    'x-locale': 'zh_CN',
    'x-site-info': '{}',
    'x-utc': '8',
    'x-zkdex-env': '0',
}

for offset in range(0,1000,20):

    params = {
        # 't': '1698996312320',
        'offset': offset,
        'txType': '',
        'limit': '20',
        'curType': '',
    }

    response = requests.get(
        'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict',
        params=params,
        cookies=cookies,
        headers=headers,
    ).text
    code = json.loads(response)
    # print(code)
    datas = code['data']['hits']
    for data in datas:
        hash = data['hash']
        time = data['blocktime']
        size = data['size']  # 交易大小
        # hash_height = data['prevBlockHeight'] # 区块高度
        print('交易哈希:', hash, '交易时间:', time, '交易大小:', size)
