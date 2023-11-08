import execjs
import requests

cookies = {
    'Hm_lvt_6088e7f72f5a363447d4bafe03026db8': '1699192812',
    'Hm_lpvt_6088e7f72f5a363447d4bafe03026db8': '1699197664',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_6088e7f72f5a363447d4bafe03026db8=1699192812; Hm_lpvt_6088e7f72f5a363447d4bafe03026db8=1699197664',
    'Origin': 'https://www.aqistudy.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC&month=201401',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
m0fhOhhGL = "GETDAYDATA"
oNLhNQ = {
    "city": "北京",
    "month": "201604"
}
hA4Nse2cT = execjs.compile(open('参数加密.js', 'r',encoding='utf-8').read()).call('post_data',m0fhOhhGL,oNLhNQ)
print(hA4Nse2cT)
data = {
    'hA4Nse2cT': hA4Nse2cT,
}

response = requests.post('https://www.aqistudy.cn/historydata/api/historyapi.php', cookies=cookies, headers=headers, data=data).text
js_code = execjs.compile(open('数据解密.js', 'r',encoding='utf-8').read()).call('dxvERkeEvHbS',response)

print(js_code)