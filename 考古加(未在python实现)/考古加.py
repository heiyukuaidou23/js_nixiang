import requests
import execjs


headers = {
    'authority': 'service.kaogujia.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJsTUQ3NHViRU9qQzgxY0lJMXpuQSIsInNpZCI6IjYxODA3NjMiLCJhdWQiOiIxMDAwIiwiaXNzIjoia2FvZ3VqaWEuY29tIiwidHlwIjoiMSIsImJ3ZSI6IjAiLCJuYmYiOjE2OTg4MzMyMTksImV4cCI6MTcwMTQyNTIxOSwiaWF0IjoxNjk4ODMzMjE5fQ.XI5YZxR9HJbmdVFwopMAnLLftqWKsmbjZruoSXRTxjk',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.kaogujia.com',
    'pragma': 'no-cache',
    'referer': 'https://www.kaogujia.com/',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    'version_code': '3.1',
    'x-utm-source': 'baidu',
    'x-utm-term': 'P_126_kgjxz',
}

params = {
    'limit': '50',
    'page': '2',
    'sort_field': 'inc_fans_count',
    'sort': '0',
}

json_data = {
    'type': 1,
    'date_code': 20231031,
    'period': '1',
    'lv1': 0,
    'province_id': 0,
    'city_id': 0,
}
url2 = '/api/rank/author/fans/increment'

response = requests.post(
    'https://service.kaogujia.com/api/rank/author/fans/increment',
    params=params,
    headers=headers,
    json=json_data,
).json()
text2 = response['data']
js_code =open('./kaogujia.js','r',encoding='utf-8').read()
code = execjs.compile(js_code).call('decrypt',text2)
print(code)