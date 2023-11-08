import json
import os
import execjs
import requests

headers = {
    'authority': 'api.zzzmh.cn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://bz.zzzmh.cn',
    'pragma': 'no-cache',
    'referer': 'https://bz.zzzmh.cn/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

for current in range(1, 10):
    json_data = {
        'size': 24,
        'current': current,
        'sort': 0,
        'category': 0,
        'resolution': 1,
        'color': 0,
        'categoryId': 0,
        'ratio': 0,
    }

    response = requests.post('https://api.zzzmh.cn/bz/v3/getData', headers=headers, json=json_data).json()
    code = response['result']
    jscode = execjs.compile(open('./jijian_bizhi.js', 'r', encoding='utf-8').read()).call('_0x18ae1d', code)
    jscode = json.loads(jscode)
    list = jscode['list']
    for data in list:
        height = data['h']
        file_name = os.path.join("imgs", data['i'] + '.jpg')
        img_href = 'https://api.zzzmh.cn/bz/v3/getUrl/' + data['i'] + '29'
        print(height, img_href)
        img = requests.get(img_href, headers=headers).content
        with open(file_name, 'wb') as file:
            file.write(img)
        print(f"下载成功：{file_name}")
