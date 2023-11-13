import execjs
import requests

cookies = {
    'btoken': 'MN8VYY1AF3PSMYLQET1J2SBRYSK27E4D',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1699629116',
    'hy_data_2020_id': '18bb9ca2c8788e-07e034dd78d411-4c657b58-1327104-18bb9ca2c88fe6',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218bb9ca2c8788e-07e034dd78d411-4c657b58-1327104-18bb9ca2c88fe6%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218bb9ca2c8788e-07e034dd78d411-4c657b58-1327104-18bb9ca2c88fe6%22%7D',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1699629190',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'btoken=MN8VYY1AF3PSMYLQET1J2SBRYSK27E4D; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1699629116; hy_data_2020_id=18bb9ca2c8788e-07e034dd78d411-4c657b58-1327104-18bb9ca2c88fe6; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218bb9ca2c8788e-07e034dd78d411-4c657b58-1327104-18bb9ca2c88fe6%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218bb9ca2c8788e-07e034dd78d411-4c657b58-1327104-18bb9ca2c88fe6%22%7D; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1699629190',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

json_data = {
    'payload': 'LBc3V0I6ZGB6bXsxTCQnPRBuBAQVcDhbICcmb2x3AjI=',
    'sig': '2FB8CF719F844A5067AD88DE1B63CEC8',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
# print(response)
jscode = execjs.compile(open('数据解密_参数加密.js', 'r', encoding='utf-8').read()).call('main123', response['d'])
print(jscode)
