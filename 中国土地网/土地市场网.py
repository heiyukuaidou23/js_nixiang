import execjs
import requests


for pageNum in range(1,10):
    Hash = execjs.compile(open('参数加密zgtdw.js','r',encoding='utf-8').read()).call('sha256')
    print(Hash)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Hash': Hash,
        'Origin': 'https://www.landchina.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.landchina.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }


    json_data = {
        'pageNum': pageNum,
        'pageSize': 10,
        'startDate': '',
        'endDate': '',
    }

    response = requests.post('https://api.landchina.com/tGdxm/result/list', headers=headers, json=json_data).json()
    print(response)