import requests
import execjs

headers = {
    'authority': 'interface.bidcenter.com.cn',
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://search.bidcenter.com.cn',
    'pragma': 'no-cache',
    'referer': 'https://search.bidcenter.com.cn/',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
}
for page in range(1, 3): #随意填写页数
    data = {
        'from': '6137',
        'guid': '52a1786b-4633-4828-93f8-52bbc862256a',
        'location': '6138',
        'token': '',
        'next_token': '',
        'keywords': '%E6%98%BE%E5%8D%A1',
        'mod': '0',
        'page': page,
    }

    response = requests.post('https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx', headers=headers, data=data).text
    # print(response)
    reslut = execjs.compile(open('./采招网2.js', 'r', encoding='utf-8').read()).call('AESDecrypt', response)
    # print(reslut)
    list_data = reslut['other2']['listData']
    for data in list_data:
        title = data['news_title_show']
        location = data['news_diqustr']
        print(title,location)
