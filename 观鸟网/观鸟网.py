import execjs
import requests


for page in range(1,10):
    data = {"limit":"20","page":page}
    js_code = execjs.compile(open('表单、参数加密gnw.js','r',encoding='utf-8').read()).call('get_data',data)
    # print(js_code)
    requestId = js_code['headers']['requestId']
    sign = js_code['headers']['sign']
    timestamp = js_code['headers']['timestamp']
    data111 = js_code['data']


    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.birdreport.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://www.birdreport.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'requestId': requestId,
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sign': sign,
        'timestamp': str(timestamp),
    }

    data1 = data111
    response = requests.post('https://api.birdreport.cn/front/activity/search', headers=headers, data=data1).json()
    result = response['data']
    js = execjs.compile(open('响应解密gnw.js','r',encoding='utf-8').read()).call('decode', result)
    print(js)