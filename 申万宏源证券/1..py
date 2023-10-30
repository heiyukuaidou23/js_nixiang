import requests

cookies = {
    'Hm_lvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c': '1698586406',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218b7ba3b005ce-0d86a314dbf86a-745d5777-1327104-18b7ba3b00610a7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiN2JhM2IwMDVjZS0wZDg2YTMxNGRiZjg2YS03NDVkNTc3Ny0xMzI3MTA0LTE4YjdiYTNiMDA2MTBhNyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218b7ba3b005ce-0d86a314dbf86a-745d5777-1327104-18b7ba3b00610a7%22%7D',
    'Hm_lpvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c': '1698586425',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c=1698586406; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218b7ba3b005ce-0d86a314dbf86a-745d5777-1327104-18b7ba3b00610a7%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThiN2JhM2IwMDVjZS0wZDg2YTMxNGRiZjg2YS03NDVkNTc3Ny0xMzI3MTA0LTE4YjdiYTNiMDA2MTBhNyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218b7ba3b005ce-0d86a314dbf86a-745d5777-1327104-18b7ba3b00610a7%22%7D; Hm_lpvt_553ce4fa7b2bd3ea6d85c1fb6b901c6c=1698586425',
    'Pragma': 'no-cache',
    'Referer': 'https://swhysc.com/swhysc/financial/marginTradingList?channel=00010017000300020001&listId=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'secuCode': '',
    'market': '',
    'onlyExchanges': '',
    'pageNum': '2',
    'pageSize': '10',
}

response = requests.get(
    'https://swhysc.com/swhyscywbl/service/dsinfo/v1/margin/conver/rate',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)