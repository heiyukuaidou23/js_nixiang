import execjs
import requests

cookies = {
    'msToken': '0RMERNrDwWRVWPBRoVOt2I6g7DPvARIXef-Sm1OuejxVa2uidXgyvTiWymtcJOUcW5eA1xZgVY6XYvVIpb_Npx8_u0cU1DdbFp1XXayh',
    '__ac_signature': '_02B4Z6wo00f01.C7hIwAAIDC4OVhtHsiFa.wm4AAAJls06',
    'tt_webid': '7299740722205705767',
    'ttcid': '7cd49df87386432a83d3599005fe709428',
    'local_city_cache': '%E9%87%8D%E5%BA%86',
    '_ga': 'GA1.1.1136047727.1699603348',
    'csrftoken': '4575c89b28148c897841174efcaae426',
    's_v_web_id': 'verify_losby8h7_kX25s3x4_34Zk_4Eg9_AOq3_CoyyR2goZGnE',
    'ttwid': '1%7C6GxrjvCRd_Uxik80KjMZG4kxvhP8N8n2qnRe3cp3X-I%7C1699718043%7C5b480dd1653138d26497a006f14e705b80d4c763382667b42bc564587509d879',
    '_ga_QEHZPBE5HH': 'GS1.1.1699720044.4.0.1699720044.0.0.0',
    'tt_scid': 'fMaNg7xdPOc8KaeOAU0nV-mGadYjngooLOEkSh2jTfwLLhE6SL0j-ceywHx2w53bf232',
}

headers = {
    'authority': 'www.toutiao.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'msToken=0RMERNrDwWRVWPBRoVOt2I6g7DPvARIXef-Sm1OuejxVa2uidXgyvTiWymtcJOUcW5eA1xZgVY6XYvVIpb_Npx8_u0cU1DdbFp1XXayh; __ac_signature=_02B4Z6wo00f01.C7hIwAAIDC4OVhtHsiFa.wm4AAAJls06; tt_webid=7299740722205705767; ttcid=7cd49df87386432a83d3599005fe709428; local_city_cache=%E9%87%8D%E5%BA%86; _ga=GA1.1.1136047727.1699603348; csrftoken=4575c89b28148c897841174efcaae426; s_v_web_id=verify_losby8h7_kX25s3x4_34Zk_4Eg9_AOq3_CoyyR2goZGnE; _ga_QEHZPBE5HH=GS1.1.1699713400.3.1.1699718043.0.0.0; tt_scid=BNGNJLCiSaQ7glbod41ilfr7NesW9BqsLeOa.GLpRIW6WZPWsPj5I3fnURE.CF0Aebe5; ttwid=1%7C6GxrjvCRd_Uxik80KjMZG4kxvhP8N8n2qnRe3cp3X-I%7C1699718043%7C5b480dd1653138d26497a006f14e705b80d4c763382667b42bc564587509d879',
    'pragma': 'no-cache',
    'referer': 'https://www.toutiao.com/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}
_signature = execjs.compile(open('./参数加密.js', 'r', encoding='utf-8').read()).call('main123')
print(_signature)
response = requests.get(
    f'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398999&min_behot_time=0&offset=0&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web&_signature={_signature}',
    cookies=cookies,
    headers=headers,
).json()
print(response)