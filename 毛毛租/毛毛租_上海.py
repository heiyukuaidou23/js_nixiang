import json
import execjs
import requests
import subprocess

import pymysql

# 设置数据库连接信息
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "js_nixiang"
}

# 连接到MySQL数据库
db = pymysql.connect(**db_config)

# 创建一个游标对象
cursor = db.cursor()

cookies = {
    'PHPSESSID': 'opo1u6q7279qfeoc8uaqiihr6k',
    'Hm_lvt_6cd598ca665714ffcd8aca3aafc5e0dc': '1698913058',
    'Hm_lpvt_6cd598ca665714ffcd8aca3aafc5e0dc': '1698916909',
    'SECKEY_ABVK': 'UmEFX7xrqEVQ61Z5SGDb4rI2duN9GCEkjWK6Z1gQr3o%3D',
    'BMAP_SECKEY': 'vWNX1lHyGxqrSYwqSSK6QG1dI-S4gMfXjvcsIdc2cd4PgHoTv-ka5ZzSXjjllx6GObDzvvYM9LDfb3NoR0ERArprQKbtdjMjzi0q0X42Thw52sjVE9OQsSZGo3JTL2hCVGWnIHXOEwFyNY0-3a3_rSambHRTCpKBsvrrMU4RwQGsPXdt85c84ojoya-4pU-P',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'PHPSESSID=opo1u6q7279qfeoc8uaqiihr6k; Hm_lvt_6cd598ca665714ffcd8aca3aafc5e0dc=1698913058; Hm_lpvt_6cd598ca665714ffcd8aca3aafc5e0dc=1698916909; SECKEY_ABVK=UmEFX7xrqEVQ61Z5SGDb4rI2duN9GCEkjWK6Z1gQr3o%3D; BMAP_SECKEY=vWNX1lHyGxqrSYwqSSK6QG1dI-S4gMfXjvcsIdc2cd4PgHoTv-ka5ZzSXjjllx6GObDzvvYM9LDfb3NoR0ERArprQKbtdjMjzi0q0X42Thw52sjVE9OQsSZGo3JTL2hCVGWnIHXOEwFyNY0-3a3_rSambHRTCpKBsvrrMU4RwQGsPXdt85c84ojoya-4pU-P',
    'Origin': 'https://www.maomaozu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.maomaozu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


# 运行JavaScript文件作为子进程
process = subprocess.Popen(['node', './maomaozu.js'], stdout=subprocess.PIPE, text=True)

# 从子进程的标准输出中获取生成的密钥
data, _ = process.communicate()
data_list = data.split(',')
for i in data_list:
    response = requests.post('https://www.maomaozu.com/index/build.json', cookies=cookies, headers=headers, data=i).text
    js_code = execjs.compile(open('./毛毛租_数据解密.js', 'r', encoding='utf-8').read()).call('aes_decrypt',response)
    datas = json.loads(js_code)
    data_list = datas['list']
    for data in data_list:
        Name = data['Name']
        Line = str(data['Line']) #路线
        Address = str(data['Address'])
        Price = data['Price'] #每平方价格
        RoomList = str(data['RoomList']) #面积
        UpdateTimeStr = data['UpdateTimeStr']
        print('名称:',Name, '路线:',Line, '地址:',Address, '价格:',Price, '面积:',RoomList)
        insert_query = "INSERT INTO maomaozu (name, Line, Address, Price, RoomList,UpdateTimeStr) VALUES (%s, %s, %s,%s, %s, %s)"
        data_tuple = (Name, Line, Address, Price, RoomList,UpdateTimeStr)

        cursor.execute(insert_query, data_tuple)

# 提交更改并关闭数据库连接
db.commit()
db.close()