import json
import re
import execjs
import requests

cookies = {
    'NMTID': '00OnDdNX4ppEepDPEaTl8v3Yfhn8LMAAAGKatVa6g',
    '_iuqxldmzr_': '32',
    '_ntes_nnid': 'e703534895f8210ead89bc126dbb62c6,1694009482485',
    '_ntes_nuid': 'e703534895f8210ead89bc126dbb62c6',
    'WEVNSM': '1.0.0',
    'WNMCID': 'tjvgow.1694009482819.01.0',
    'ntes_utid': 'tid._.ezWyqaNWYNxERxRUBEKRzD3I5iYsoGmr._.0',
    'WM_TID': 'ZF%2BD3jlMXOhAUEVAVVOB2GmYonJptNg8',
    'sDeviceId': 'YD-bxRbBZMfk0NBUxBQRUeVaSbGEIuHmdNF',
    'ntes_kaola_ad': '1',
    'JSESSIONID-WYYY': 'dNsonSm9I3YDa56DQ0NSbjBY%2B1wtfDj%2F2q9zdyvBlfaARRrdEszX%2F61mZNQf5%2F14tgDQunk98BIKcqECn3ZiYsPqpJXdg5CASglarKD93nMmqBislQsxkEAx%2BSChVfsmY0FacuMFfqnI0q091jGkqhYX6JE4gaWmij345U80JMR8%2FWpl%3A1699536382510',
    'WM_NI': 'wnZnYHonpWynSTkMTK%2FWWhox28pcKD%2B2qHbwXwrMeJoplAjR4wfkpDW1M3G9NHqGtc93%2Ba7b9nGxO3mfpv59yO%2FusQZjz%2B2fB8r%2B5mx87ZVxBqxYr1LAWY%2BigEd84LkZcWw%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eebac579a6ba8396cb5fa9ac8fb2d14f928f8bb1c139b1b1a4a8cb3e94b0faaac52af0fea7c3b92ab5b2968fdc44adb2c0b8fc66918ca5aed741ed899989ee74f2e8c084ca50e9eebfa9e17d9ca9beaee842adb0a4a2e95af8a9aa8cf35095ef83d4c6338e98bfa8f769fbede582b66afbb28999ce39afbac097b833bb91e196f25b9ab6b6ccb16e82e8beccb867bce8f9bbd57482afb8baf13b909f99baaa63a59bacd9b748a986adb8f637e2a3',
    'playerid': '82666398',
}

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'NMTID=00OnDdNX4ppEepDPEaTl8v3Yfhn8LMAAAGKatVa6g; _iuqxldmzr_=32; _ntes_nnid=e703534895f8210ead89bc126dbb62c6,1694009482485; _ntes_nuid=e703534895f8210ead89bc126dbb62c6; WEVNSM=1.0.0; WNMCID=tjvgow.1694009482819.01.0; ntes_utid=tid._.ezWyqaNWYNxERxRUBEKRzD3I5iYsoGmr._.0; WM_TID=ZF%2BD3jlMXOhAUEVAVVOB2GmYonJptNg8; sDeviceId=YD-bxRbBZMfk0NBUxBQRUeVaSbGEIuHmdNF; ntes_kaola_ad=1; JSESSIONID-WYYY=dNsonSm9I3YDa56DQ0NSbjBY%2B1wtfDj%2F2q9zdyvBlfaARRrdEszX%2F61mZNQf5%2F14tgDQunk98BIKcqECn3ZiYsPqpJXdg5CASglarKD93nMmqBislQsxkEAx%2BSChVfsmY0FacuMFfqnI0q091jGkqhYX6JE4gaWmij345U80JMR8%2FWpl%3A1699536382510; WM_NI=wnZnYHonpWynSTkMTK%2FWWhox28pcKD%2B2qHbwXwrMeJoplAjR4wfkpDW1M3G9NHqGtc93%2Ba7b9nGxO3mfpv59yO%2FusQZjz%2B2fB8r%2B5mx87ZVxBqxYr1LAWY%2BigEd84LkZcWw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebac579a6ba8396cb5fa9ac8fb2d14f928f8bb1c139b1b1a4a8cb3e94b0faaac52af0fea7c3b92ab5b2968fdc44adb2c0b8fc66918ca5aed741ed899989ee74f2e8c084ca50e9eebfa9e17d9ca9beaee842adb0a4a2e95af8a9aa8cf35095ef83d4c6338e98bfa8f769fbede582b66afbb28999ce39afbac097b833bb91e196f25b9ab6b6ccb16e82e8beccb867bce8f9bbd57482afb8baf13b909f99baaa63a59bacd9b748a986adb8f637e2a3; playerid=82666398',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

top_url = 'https://music.163.com/discover/toplist?id=3779629'

# print(data)

data11 = requests.get(url=top_url,headers=headers).text
# print(data11)
top_url_list = re.findall('<a class="avatar" href="/discover/toplist(.*?)">',data11)
# print(top_url_list)
for top_urls in top_url_list:
    top_href = top_urls.strip('?id=')
    # print(top_href)
    type_url = 'https://music.163.com/discover/toplist?id=' + top_href
    # print(type_url)
    res = requests.get(url=type_url,headers=headers).text
    song_ids = re.findall('<li><a href="/(.*?)">(.*?)</a>',res)
    # print(song_ids)
    for song_id in song_ids:
        music_id = song_id[0].strip('/song?id=')
        music_name1 = song_id[1]
        music_name = re.sub(r'[\/:*?"<>|]', '_', music_name1)
        # print(music_id,music_name)

        encSecKey = execjs.compile(open('参数加密enc.js', 'r', encoding='utf-8').read()).call('main123', music_id)
        # print(encSecKey)
        params = {
            'csrf_token': '',
        }

        data = {
            'params': encSecKey['encText'],
            'encSecKey': encSecKey['encSecKey'],
        }

        response = requests.post(
            'https://music.163.com/weapi/song/enhance/player/url/v1',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).text
        # print(response)
        data_music = json.loads(response)
        if data_music.get('data') and data_music['data'][0].get('url'):
            mp3_url = data_music['data'][0]['url']
            # print(mp3_url)
            music = requests.get(mp3_url, headers=headers).content
            with open(f'./music/{music_name}.mp3', 'wb') as f:
                f.write(music)
                print(f'下载完成{music_name}.mp3')
        else:
            print(f'{music_name}的mp3_url为None，跳过下载')