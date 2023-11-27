# coding: utf-8
# Project：JS逆向
# File：2.看准.py
# Author：下雨天
# Date ：2023/11/18 16:46
import execjs
import requests

cookies = {
    'wd_guid': '4ad9b138-986f-4420-8925-eebdc7314cf5',
    'historyState': 'state',
    '__c': '1700291797',
    '__g': '-',
    '__l': 'l=%2Fwww.kanzhun.com%2Fsearch%3FpageNum%3D1%26query%3D%25E7%2588%25AC%25E8%2599%25AB%26type%3D1&r=',
    'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1699243131,1700291797',
    '__lh_v1': '5_0',
    'R_SCH_CY_V': '11514',
    'W_CITY_S_V': '9',
    'pageType': '1',
    'lasturl': '"https://www.kanzhun.com/rank_f/"',
    't': 'GPUNl35eTqFgz2r',
    '__a': '79720225.1699243128.1699243128.1700291797.39.2.20.39',
    'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1700295692',
}

headers = {
    'authority': 'www.kanzhun.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': 'wd_guid=4ad9b138-986f-4420-8925-eebdc7314cf5; historyState=state; __c=1700291797; __g=-; __l=l=%2Fwww.kanzhun.com%2Fsearch%3FpageNum%3D1%26query%3D%25E7%2588%25AC%25E8%2599%25AB%26type%3D1&r=; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1699243131,1700291797; __lh_v1=5_0; R_SCH_CY_V=11514; W_CITY_S_V=9; pageType=1; lasturl="https://www.kanzhun.com/rank_f/"; t=GPUNl35eTqFgz2r; __a=79720225.1699243128.1699243128.1700291797.39.2.20.39; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1700295692',
    'href': 'https://www.kanzhun.com/rank_f/',
    'pragma': 'no-cache',
    'referer': 'https://www.kanzhun.com/rank_f/',
    'reqsource': 'fe',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceid': '037f961d-e074-4637-97f4-256e1f3c3baf',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}
data = '{"cityCode":"","industryCode":"","curPage":1}'
kiv = execjs.compile(open('2.参数加密.js', 'r', encoding='utf-8').read()).call('kiv')
print(kiv)
t = {
    "iv": kiv
}
b = execjs.compile(open('2.参数加密.js', 'r', encoding='utf-8').read()).call('main123', data, t)
print(b)
params = {
    'b': b,
    'kiv': kiv,
}

response = requests.get(
    'https://www.kanzhun.com/api_to/channel/company/list.json',
    params=params,
    cookies=cookies,
    headers=headers,
).text
# print(response)
res = execjs.compile(open('2.参数加密.js', 'r', encoding='utf-8').read()).call('c', response,t)
print(res)
