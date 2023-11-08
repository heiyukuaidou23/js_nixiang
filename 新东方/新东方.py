import execjs
import requests

from datetime import datetime

# 获取当前时间
current_time = datetime.now()

# 将当前时间转换为精确到毫秒的时间戳
timestamp = int(current_time.timestamp() * 1000)

print(timestamp)

sign = execjs.compile(open('参数加密xdf.js','r',encoding='utf-8').read()).call('main123',timestamp)
print(sign)
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://souke.xdf.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://souke.xdf.cn/search?cityCode=500100&categoryCode=54',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': sign,
}

params = {
    'appId': '5053',
    'cityCode': '500100',
    't': timestamp,
    'pageIndex': '1',
    'pageSize': '12',
    'categoryCode': '54',
    'order': '0',
}

response = requests.get('https://dsapi.xdf.cn/product/v2/class/search', params=params, headers=headers).json()
print(response)
