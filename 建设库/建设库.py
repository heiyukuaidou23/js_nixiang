import execjs
import requests

from datetime import datetime


cookies = {
    'Hm_lvt_03b8714a30a2e110b8a13db120eb6774': '1699077307',
    'UM_distinctid': '18b98e639026d8-0d472d388a5752-4c657b58-144000-18b98e639031067',
    'HWWAFSESTIME': '1699077306445',
    'HWWAFSESID': 'd86608be1b23b7698c',
    'Hm_lpvt_03b8714a30a2e110b8a13db120eb6774': '1699077372',
}





for page in range(1, 10):
    jscode = execjs.compile(open('./jiansheku.js', 'r', encoding='utf-8').read()).call('generateSign', page)
    print(jscode)
    # 获取当前时间
    current_time = datetime.now()

    # 将当前时间转换为精确到毫秒的时间戳
    timestamp = current_time.timestamp() * 1000
    print(timestamp)
    headers = {
        'authority': 'capi.jiansheku.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'Hm_lvt_03b8714a30a2e110b8a13db120eb6774=1699077307; UM_distinctid=18b98e639026d8-0d472d388a5752-4c657b58-144000-18b98e639031067; HWWAFSESTIME=1699077306445; HWWAFSESID=d86608be1b23b7698c; Hm_lpvt_03b8714a30a2e110b8a13db120eb6774=1699077372',
        'devicetype': 'PC',
        'origin': 'https://www.jiansheku.com',
        'page': 'search-enterprise',
        'pragma': 'no-cache',
        'referer': 'https://www.jiansheku.com/',
        'region': 'nation_zhujian',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sign': jscode,
        'timestamp': str(timestamp),
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    }
    json_data = {
        'eid': '',
        'achievementQueryType': 'and',
        'achievementQueryDto': [],
        'personnelQueryDto': {
            'queryType': 'and',
        },
        'aptitudeQueryDto': {
            'queryType': 'and',
            'nameStr': '',
            'aptitudeQueryType': 'and',
            'businessScopeQueryType': 'or',
            'filePlaceType': '1',
            'aptitudeDtoList': [
                {
                    'codeStr': '',
                    'queryType': 'and',
                    'aptitudeType': 'qualification',
                },
            ],
            'aptitudeSource': 'new',
        },
        'page': {
            'page': page,
            'limit': 20,
            'field': '',
            'order': '',
        },
    }

    response = requests.post('https://capi.jiansheku.com/nationzj/enterprice/page', cookies=cookies, headers=headers, json=json_data).json()
    # print(response)
    data = response['data']['list']
    for info in data:
        company_name = info['name']
        legalPerson = info['legalPerson'] #法人代表
        registeredCapital = info['registeredCapital']   #注册资本
        businessAddress = info['businessAddress']
        registeredDate = info['registeredDate'] # 成立日期
        print(company_name, legalPerson, registeredCapital, businessAddress, registeredDate)