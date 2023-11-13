
import execjs
import requests

cookies = {
    'mobile_iindex_uuid': '2c73ce90-eca5-5683-a934-b4e18ed1f78a',
    'Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f': '1699689431',
    'Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f': '1699689779',
}

headers = {
    'authority': 'www.chinaindex.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'mobile_iindex_uuid=2c73ce90-eca5-5683-a934-b4e18ed1f78a; Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f=1699689431; Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f=1699689779',
    'funcid': 'undefined',
    'incognitomode': '0',
    'pragma': 'no-cache',
    'referer': 'https://www.chinaindex.net/ranklist/5/1',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'uuid': '2c73ce90-eca5-5683-a934-b4e18ed1f78a',
}



params = {
    'sign': '46cf510e48f99667216bfa781d6bebab',
}

response = requests.get(
    'https://www.chinaindex.net/iIndexMobileServer/teleplay/rank/playing/fans',
    params=params,
    cookies=cookies,
    headers=headers,
).json()
# print(response)
data = response['data']
lastfetchtime = response['lastFetchTime']
jscode = execjs.compile(open('./参数加密.js', 'r', encoding='utf-8').read()).call('main123', data, lastfetchtime)
print(jscode)