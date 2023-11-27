import requests
import execjs



json_data = {
    'keyword': '',
    'provinceNames': [],
    'natureTypes': [],
    'eduLevel': '',
    'categories': [],
    'features': [],
    'pageIndex': 2,
    'pageSize': 20,
    'sort': 11,
}

u_sign = execjs.compile(open('参数加密yzy.js','r',encoding='utf-8').read()).call('main123',json_data)
print(u_sign)
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://pv4y-pc.youzy.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://pv4y-pc.youzy.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'u-sign': u_sign,
    'u-token': '',
}



response = requests.post(
    'https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query',
    headers=headers,
    json=json_data,
)
print(response.text)
