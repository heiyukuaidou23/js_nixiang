import json
import re

import execjs
import requests

cookies = {
    'aliyungf_tc': '1fabe19ecd33b24c1164e94e98459ffa40a0637a8a9bf48ba3de3124c52175aa',
    'Hm_lvt_1684191ccae0314c6254306a8333d090': '1699282856',
    'Hm_lvt_713123c60a0e86982326bae1a51083e1': '1699282856',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218ba526a86ce8e-058ba16eec0067-4c657b58-1327104-18ba526a86df59%22%2C%22%24device_id%22%3A%2218ba526a86ce8e-058ba16eec0067-4c657b58-1327104-18ba526a86df59%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'acw_tc': 'ac11000116992866513761502e5a0e939685eb6b2ce3e5e228892c2184e22d',
    'Hm_lpvt_1684191ccae0314c6254306a8333d090': '1699287217',
    'Hm_lpvt_713123c60a0e86982326bae1a51083e1': '1699287217',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'aliyungf_tc=1fabe19ecd33b24c1164e94e98459ffa40a0637a8a9bf48ba3de3124c52175aa; Hm_lvt_1684191ccae0314c6254306a8333d090=1699282856; Hm_lvt_713123c60a0e86982326bae1a51083e1=1699282856; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218ba526a86ce8e-058ba16eec0067-4c657b58-1327104-18ba526a86df59%22%2C%22%24device_id%22%3A%2218ba526a86ce8e-058ba16eec0067-4c657b58-1327104-18ba526a86df59%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; acw_tc=ac11000116992866513761502e5a0e939685eb6b2ce3e5e228892c2184e22d; Hm_lpvt_1684191ccae0314c6254306a8333d090=1699287217; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1699287217',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.36kr.com/p/2506753915446658', cookies=cookies, headers=headers).text
# print(response)
res = re.findall('<script>window.initialState=(.*?)</script>', response)
# print(res)
state = res[0]
# print(state)
data2 = state.replace('isEncrypt','').replace(',"":true','')
# data1 = json.dumps(data2)

print(data2)
# data = data1['state']
# print(data)
ex = execjs.compile(open('36kr_数据解密.js','r',encoding='utf-8').read()).call('decryptAndLogData',data2)
print(ex)
