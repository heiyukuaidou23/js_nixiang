import json
import time

import pymysql
import requests
import execjs

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

for pn in range(1, 100):
    data1 = {"first": "true", "needAddtionalResult": "false", "city": "全国", "pn": pn, "fromSearch": "true",
             "kd": "java"}
    js_code = open('./lagou.js', 'r', encoding='utf-8').read()
    X_S = execjs.compile(js_code).call('HeaderEncrypt', data1)
    # print(X_S)

    Body_data = execjs.compile(js_code).call('BodyEncrypt', data1)
    print(Body_data)

    cookies = {
        'RECOMMEND_TIP': 'true',
        'user_trace_token': '20230908085744-1b9f02f5-947c-4bbf-b459-2d7efaf637f5',
        'LGUID': '20230908085744-b29a25f3-610f-443e-a76e-30f194775281',
        '_ga': 'GA1.2.1852773080.1694134664',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1696497331,1697168377,1698745954,1698819764',
        '_ga_DDLTLJDLHH': 'GS1.2.1698819765.6.1.1698819779.46.0.0',
        'LG_HAS_LOGIN': '1',
        '__lg_stoken__': '339f4b2b746d325b273eeb0091826e9ca00a20cfc86fa0e991959dfcd0c0910cd823b2189183a4d8901d986329fb070f7ca6bd16f0be8ec9fe3cce12d48feca3af74c14e846f',
        'X_HTTP_TOKEN': '780a9bfe69f60d854252789961bf3b0f99cb15c9f1',
        'WEBTJ-ID': '20231113184848-18bc84c56964aa-01e8ee5ff6d6e4-4c657b58-1327104-18bc84c56971264',
        'JSESSIONID': 'ABAAABAABEIABCI9DF461A35D62244E5BB6337AC265F0C8',
        'sensorsdata2015session': '%7B%7D',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218a724b7c4e101c-074f091f3ffd7b-7f5d5470-1327104-18a724b7c4f133d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22119.0.0.0%22%7D%2C%22%24device_id%22%3A%2218a724b7c4e101c-074f091f3ffd7b-7f5d5470-1327104-18a724b7c4f133d%22%7D',
    }

    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'RECOMMEND_TIP=true; user_trace_token=20230908085744-1b9f02f5-947c-4bbf-b459-2d7efaf637f5; LGUID=20230908085744-b29a25f3-610f-443e-a76e-30f194775281; _ga=GA1.2.1852773080.1694134664; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABAGABFAD58C0C7BC85740550EBA5285A3EEF7F1; WEBTJ-ID=20231031175233-18b85262b56984-06dbe7bad20759-745d5777-1327104-18b85262b5710a2; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1696488312,1696497331,1697168377,1698745954; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1698745954; sensorsdata2015session=%7B%7D; _gid=GA1.2.1001350177.1698745954; privacyPolicyPopup=false; _ga_DDLTLJDLHH=GS1.2.1698745954.5.0.1698745954.60.0.0; TG-TRACK-CODE=index_search; LGRID=20231031175243-6fd8a60b-50cf-4f52-b6e4-518a489a7098; X_HTTP_TOKEN=780a9bfe69f60d853695478961bf3b0f99cb15c9f1; X_MIDDLE_TOKEN=4c03893e66b1cada4768663ac267f67a; __lg_stoken__=4e5259110056cace9abfd2283f9f87f749f17e523825487f3dda52ff2c11528973cfefcd5021bc5df9fae93e21f2dd3a143aa75c57e3a2bc2859aa33b38b6d5533ad2b9e1b4e; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218a724b7c4e101c-074f091f3ffd7b-7f5d5470-1327104-18a724b7c4f133d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22118.0.0.0%22%7D%2C%22%24device_id%22%3A%2218a724b7c4e101c-074f091f3ffd7b-7f5d5470-1327104-18a724b7c4f133d%22%7D',
        'Origin': 'https://www.lagou.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.lagou.com/wn/jobs?pn=5&fromSearch=true&kd=python',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        'X-K-HEADER': 'vU6VJmd9yv3K/d4L+Zs61xEITko6rQZRW8rI62kLUwI0Fshd02M8U96lkmeUsd+3',
        'X-S-HEADER': X_S,
        'X-SS-REQ-HEADER': '{"secret":"vU6VJmd9yv3K/d4L+Zs61xEITko6rQZRW8rI62kLUwI0Fshd02M8U96lkmeUsd+3"}',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'traceparent': '00-29b9838c423dcbc85d35b00561b24442-306ba9b06d278302-01',
        'x-anit-forge-code': '0',
        'x-anit-forge-token': 'None',
    }
    # 加密
    data = {
        'data': Body_data,
    }

    response = requests.post('https://www.lagou.com/jobs/v2/positionAjax.json', cookies=cookies, headers=headers,
                             data=data).json()
    print(response)
    t = response['data']
    # print(t)
    js = open('./tt.js', 'r', encoding='utf-8').read()
    # print(js)
    result = execjs.compile(js).call('decryptData', t)
    job_list = json.loads(result)
    # print(result)
    # data = response['data']
    # print(data)
    jobs = job_list['content']['positionResult']['result']

    for job in jobs:
        job_name = job['positionName']
        company_name = job['companyFullName']
        company_size = job['companySize']
        welfare = str(['companyLabelList'])  # 福利
        job_type = job['firstType']
        create_time = job['createTime']
        job_salary = job['salary']
        city = job['city']
        linestaion = job['linestaion']  # 工作地点
        job_detail = job['positionDetail'].replace('<br />', '').replace('<br/>', '').replace('<p>', '').replace('</p>','').replace('\n','')
        print(job_name, company_name, company_size, welfare, job_type, create_time, job_salary, job_detail)
        # 插入数据到数据库表
        insert_query = "INSERT INTO lagou_jobs_copy1 (job_name, company_name, company_size, welfare, job_type, create_time, job_salary, city,linestaion,job_detail) VALUES (%s,%s,%s, %s, %s, %s, %s,%s, %s,%s)"
        data_tuple = (job_name, company_name, company_size, welfare, job_type, create_time, job_salary, city,linestaion, job_detail)

        cursor.execute(insert_query, data_tuple)
        time.sleep(1)

# 提交更改并关闭数据库连接
db.commit()
db.close()
