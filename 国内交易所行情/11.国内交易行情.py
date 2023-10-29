import requests
import execjs

import pymysql

# 设置数据库连接信息
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "gupiao_info"
}

# 连接到MySQL数据库
db = pymysql.connect(**db_config)

# 创建一个游标对象
cursor = db.cursor()

cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1698284239,1698564534',
    'MALLSSID': '5A63754B654170526463536237574859562F73493143766D58414F4334684F4C5356476A6C48734B3651426B484E6C6B3172774752435839696159456F496557',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1698569119',
}

EncKey = execjs.compile(open('11.国内交易行情.js', 'r', encoding='utf-8').read()).call('getResCode')
print(EncKey)

headers = {
    'Accept': '*/*',
    'Accept-EncKey': EncKey,
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1698284239,1698564534; MALLSSID=5A63754B654170526463536237574859562F73493143766D58414F4334684F4C5356476A6C48734B3651426B484E6C6B3172774752435839696159456F496557; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1698569119',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'tdate': '2023-10-26',
    'market': 'SZE',
}

response = requests.post('https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007', cookies=cookies, headers=headers,
                         data=data).json()
# print(response)
text = response['records']
for res in text:
    name = res['证券简称']
    date = res['交易日期']
    place = res['交易所']
    currency = res['币种']
    Opening = res['开盘价']
    Closing = res['收盘价']
    code = res['证券代码']
    number = res['成交数量']
    low_price = res['最低价']
    high_price = res['最高价']
    price = res['成交金额']
    print(name, date, place, currency, Opening, Closing, code, number, low_price, high_price, price)
    # 插入数据到数据库表
    insert_query = "INSERT INTO gupiao (name, date,place,currency,Opening,Closing,code, number, low_price, high_price, price) VALUES (%s, %s,%s, %s, %s, %s,%s, %s,%s, %s, %s)"
    data_tuple = (name, date, place,currency,Opening,Closing,code, number, low_price, high_price, price)

    cursor.execute(insert_query, data_tuple)

# 提交更改并关闭数据库连接
db.commit()
db.close()
