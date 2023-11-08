import execjs
import requests

headers = {
    'authority': 'api.eol.cn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.gaokao.cn',
    'pragma': 'no-cache',
    'referer': 'https://www.gaokao.cn/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

for page in range(1, 10):
    signsafe = execjs.compile(open('参数加密zsgk.js','r',encoding='utf-8').read()).call('main123',page)
    print('当前page是',page)
    print(signsafe)
    json_data = {
        'keyword': '',
        'page': page,
        'province_id': '',
        'ranktype': '',
        'request_type': 1,
        'signsafe': signsafe,
        'size': 20,
        'top_school_id': '1476,184,101,2691,1181',
        'type': '',
        'uri': 'apidata/api/gkv3/school/lists',
    }

    response = requests.post(
        f'https://api.eol.cn/web/api/?keyword=&page={page}&province_id=&ranktype=&request_type=1&size=20&top_school_id=1476,184,101,2691,1181&type=&uri=apidata/api/gkv3/school/lists&signsafe={signsafe}',
        headers=headers,
        data=json_data,
    ).json()
    print(response)
