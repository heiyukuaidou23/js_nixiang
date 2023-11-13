import json
import time

import execjs
import requests


from datetime import datetime

current_time = datetime.now()
timestamp = int(current_time.timestamp() * 1000)
print(timestamp)
# timestamp = int(time.time()*1000)
cookies = {
    'miid': '658036801754566009',
    'thw': 'cn',
    't': '82127e0c71c79c2739bfa6f124d16e34',
    '_tb_token_': '83ee13571413',
    'cna': 'qniFHSKv72UCAbdFjZ3Q2caY',
    'xlly_s': '1',
    'cookie2': '1f7ca8b883dec43bad2f3249dd7597be',
    '_samesite_flag_': 'true',
    'sgcookie': 'E100EeX2ExCs2NUHwtrA1o2K2X0xrQBizQDq4zKli7ffIa%2FZ3%2Fpb82P4b6eU2xV4MWTbdAky08byBWBKaPvWpJ0YEyfKmqHrY8Cp7kI4jfDB1cQ%3D',
    'unb': '3326796581',
    'uc3': 'lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD3CIZ0wj%2FYvJm7X8%3D&id2=UNN%2F6l3Nkrtvdg%3D%3D&nk2=yxAOtfINVEKxE0TbrnipSn%2F2',
    'csg': 'ff52b51f',
    'lgc': '%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4',
    'cancelledSubSites': 'empty',
    'cookie17': 'UNN%2F6l3Nkrtvdg%3D%3D',
    'dnk': '%5Cu8096%5Cu5947%5Cu4F26xqlun',
    'skt': 'c9b308687e46db68',
    'existShop': 'MTY5OTY4MjE3Mg%3D%3D',
    'uc4': 'id4=0%40UgQ3BdKawHgAB9Z7r%2Fn%2BrcjXhKgy&nk4=0%40ySlAcaTuheswgUPc6Shw%2B3KBWONUU1nWuDFvXDM%3D',
    'tracknick': '%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4',
    '_cc_': 'UIHiLt3xSw%3D%3D',
    '_l_g_': 'Ug%3D%3D',
    'sg': '%E5%B7%B41d',
    '_nk_': '%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4',
    'cookie1': 'Vy0Vzmb8naRYzvJNN1XCN55Q5E1L1SO7ceqWi63rb1I%3D',
    'mt': 'ci=33_1',
    'uc1': 'cookie21=U%2BGCWk%2F7p4sj&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=Uoe9ZL5UrKZCAQ%3D%3D',
    'l': 'fBjZ-zFuPs5O3jXpBOfanurza77OkIRbmuPzaNbMi9fP9I1p5coPW1Fnn289CnGVEsWFk3utAYh6BfLL_yUIQxv9-e6jmk0GsdTn4Qipf',
    'tfstk': 'd6IwkmY3PlEZkCR_yFx2Yz4B9Zx9c3FSIiOXntXDCCAGcdbF0BWuBCaYWs7Fi6L6sPKfn6WVgm_6jcGmiBXbBmwOI-rVnTAGCtNx0xAFsmT1Gi7K0TBAfRKbBhB9DnV7Nu1VBOKvJWGQR_xtiwSng7Z7VOFWiZ7LNRKTdQj_KCgZM7YUZTAhXYSn1_EjTBmmmGqAzQ-ilmo2adYNqOXZWjphsoSA7j02SppeNJyUPbTt7',
    'isg': 'BPf3mkKRXoH9T9oNLxg3oWgbhutBvMseLOmX3UmkE0Yt-Bc6UIxbbrWZ3l6mFKOW',
    '_m_h5_tk': 'b597150d58fb71aafc1cca0fe7fb9203_1699711568514',
    '_m_h5_tk_enc': '15d34d6c6d8251f6ff7497b779bc538a',
}

headers = {
    'authority': 'h5api.m.taobao.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'miid=658036801754566009; thw=cn; t=82127e0c71c79c2739bfa6f124d16e34; _tb_token_=83ee13571413; cna=qniFHSKv72UCAbdFjZ3Q2caY; xlly_s=1; cookie2=1f7ca8b883dec43bad2f3249dd7597be; _samesite_flag_=true; sgcookie=E100EeX2ExCs2NUHwtrA1o2K2X0xrQBizQDq4zKli7ffIa%2FZ3%2Fpb82P4b6eU2xV4MWTbdAky08byBWBKaPvWpJ0YEyfKmqHrY8Cp7kI4jfDB1cQ%3D; unb=3326796581; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dD3CIZ0wj%2FYvJm7X8%3D&id2=UNN%2F6l3Nkrtvdg%3D%3D&nk2=yxAOtfINVEKxE0TbrnipSn%2F2; csg=ff52b51f; lgc=%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4; cancelledSubSites=empty; cookie17=UNN%2F6l3Nkrtvdg%3D%3D; dnk=%5Cu8096%5Cu5947%5Cu4F26xqlun; skt=c9b308687e46db68; existShop=MTY5OTY4MjE3Mg%3D%3D; uc4=id4=0%40UgQ3BdKawHgAB9Z7r%2Fn%2BrcjXhKgy&nk4=0%40ySlAcaTuheswgUPc6Shw%2B3KBWONUU1nWuDFvXDM%3D; tracknick=%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%B7%B41d; _nk_=%5Cu02CA%5Cu30C5%5Cu9189%5Cu7231%5Cu706C%5Cu8FEA%5Cu4E3D%5Cu70ED%5Cu5DF4; cookie1=Vy0Vzmb8naRYzvJNN1XCN55Q5E1L1SO7ceqWi63rb1I%3D; _m_h5_tk=3bc1b6b492649699631595675cd1223d_1699702134652; _m_h5_tk_enc=60a76125c6c77967b61b8e2657303f63; x5sec=7b22617365727665723b32223a226661303534653231386638376639313761303239303432663732313664366432434f577176616f47454d36586a4b55464767777a4d7a49324e7a6b324e5467784f7a4d6f674151777674476d72415a4141773d3d222c22733b32223a2236356333396361613563366564303730227d; mt=ci=33_1; uc1=cookie21=U%2BGCWk%2F7p4sj&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=Uoe9ZL5UrKZCAQ%3D%3D; l=fBjZ-zFuPs5O3caTBO5Courza779ZIRfCoVzaNbMiIEGa6sdtib6DNCTtAGeSdtjgTCD_eKrWDM-1dFX8eUdNxDDBefNWqisnxYx2p7lW; tfstk=dnoDl8cAWqzfCiVmRIEX0LD8nk88lsZ_nfIT6lFwz7PS6ZkZH42Z6b96hoHasfc8NKNTXozajvG3gsIADb4Z6vuYuf3Y_RPriPn9hG3lIvGuXfD6hRPZ_fVtkUKKhxZ_bBEMvHHj3Op-mOjACL6YflRp9_O02MZstS_6MGn1zezP2090-WX67S2VEMRUOxPlxYiz3ZPHASSNb04inYBwsa7EqES_UdnP5Na4F8Vd3_bFm; isg=BGtrPO9Oiv2y4NYp29QDDYSf-o9VgH8CcO2b-d3oR6r6fIveZVAPUgmd0roS2Nf6',
    'pragma': 'no-cache',
    'referer': 'https://h5.m.taobao.com/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 Edg/119.0.0.0',
}
data = '{"showTrueCount": false, "auctionNumId": "652797551998", "rateType": "", "searchImpr": "-8", "expression": "","orderType": "", "pageSize": 10, "pageNo": 2}'
jscode = execjs.compile(open('./参数加密.js', 'r', encoding='utf-8').read()).call('main123',timestamp,data)
print(jscode)
params = {
    'jsv': '2.7.0',
    'appKey': '12574478',
    't': timestamp,
    'sign': jscode,
    'api': 'mtop.taobao.rate.detaillist.get',
    'v': '6.0',
    'ecode': '1',
    'type': 'jsonp',
    'timeout': '20000',
    'dataType': 'jsonp',
    'sessionOption': 'AutoLoginOnly',
    'jsonpIncPrefix': 'haloMtop',
    'callback': 'mtopjsonphaloMtop7',
    'data': '{"showTrueCount":false,"auctionNumId":"652797551998","rateType":"","searchImpr":"-8","expression":"","orderType":"","pageSize":10,"pageNo":1}',
}

response = requests.get(
    'https://h5api.m.taobao.com/h5/mtop.taobao.rate.detaillist.get/6.0/',
    params=params,
    cookies=cookies,
    headers=headers,
).text
print(response)