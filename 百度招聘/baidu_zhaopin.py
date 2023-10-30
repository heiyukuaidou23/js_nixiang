import requests
import re
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
    'BAIDUID': 'FD88D696021FAD018210A4208D116EB7:FG=1',
    'BAIDUID_BFESS': 'FD88D696021FAD018210A4208D116EB7:FG=1',
    'newlogin': '1',
    'BIDUPSID': 'FD88D696021FAD018210A4208D116EB7',
    '__bid_n': '18b616a50d646083c4a2c9',
    'RT': '"z=1&dm=baidu.com&si=3509e39f-47ce-4b21-ad81-02ce18bd38ca&ss=lo48jliv&sl=1&tt=3cn&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=7iyy&hd=7izb"',
    'BDUSS': 'ZTWGpYTW9SbUdtSVRDdzJQZTdYV0Y3VlQzMHN3UGlqLTBYQXk4cnFyQmJaR0JsSVFBQUFBJCQAAAAAAAAAAAEAAAABoTqXNTW6x7rHzabU2gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFvXOGVb1zhlZ0',
    'BDUSS_BFESS': 'ZTWGpYTW9SbUdtSVRDdzJQZTdYV0Y3VlQzMHN3UGlqLTBYQXk4cnFyQmJaR0JsSVFBQUFBJCQAAAAAAAAAAAEAAAABoTqXNTW6x7rHzabU2gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFvXOGVb1zhlZ0',
    'Hm_lvt_e3eec7019ba4d61b236c8afa00fd2ca4': '1696254346,1698592096,1698648135',
    'SECKEY_ABVK': 'Vq5sqWvL9/KRFSHkrXmVh2arr/08mRgAUJL60xiOOTMtDaUJ/llhBnM3FDclVf6xO+tPYLeOhxV1NF1fBGQxKQ%3D%3D',
    'Hm_lpvt_e3eec7019ba4d61b236c8afa00fd2ca4': '1698649835',
    'ab_sr': '1.0.1_OTFlZDhkNWU5MmIyZTBhNTI5MTZiNmY5MGEzYWUwMTA2OThiYjkyZWRhNTFlNmQ1N2Q4MTU2ZDFmMWU3MGM1YzBkM2ViNmQ1YjAzNzY3ZTVkZmZmNDA2ZjdkNjJiYzYwZWU4MDMxNjU5ZDYwZWFmZGQzYWEyZThlMzMxZWFhZjQ3ZjkyYTkzMDYyMmExYWRjZWRiYzUyMTZjZWRlYzM2ODMyMGI0NTNhMTlmNDY4ZDY5NGE3MGU0NDQ4OWZjY2M5',
    'BMAP_SECKEY': 'jxxImVi5nZOFLBbqjTfHHqjF2Xej5X-sZYUCzoonbSYqkAvDhVHX_xQtoAgBZP--8ypnbV2L4EIFBpqzs56nQ6opZ9miYxEjX5A7A6peI2ZWvDfd9Ktj-flWUUMz2QrU5EG_CvpMzC_v4o0LNLZF4gPGtMMpYhnk_zpGkJHEtNrpqoZeaTog6mXL_ajlM1ws',
}

headers = {
    'authority': 'zhaopin.baidu.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    # 'cookie': 'BAIDUID=FD88D696021FAD018210A4208D116EB7:FG=1; BAIDUID_BFESS=FD88D696021FAD018210A4208D116EB7:FG=1; newlogin=1; BIDUPSID=FD88D696021FAD018210A4208D116EB7; __bid_n=18b616a50d646083c4a2c9; RT="z=1&dm=baidu.com&si=3509e39f-47ce-4b21-ad81-02ce18bd38ca&ss=lo48jliv&sl=1&tt=3cn&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=7iyy&hd=7izb"; BDUSS=ZTWGpYTW9SbUdtSVRDdzJQZTdYV0Y3VlQzMHN3UGlqLTBYQXk4cnFyQmJaR0JsSVFBQUFBJCQAAAAAAAAAAAEAAAABoTqXNTW6x7rHzabU2gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFvXOGVb1zhlZ0; BDUSS_BFESS=ZTWGpYTW9SbUdtSVRDdzJQZTdYV0Y3VlQzMHN3UGlqLTBYQXk4cnFyQmJaR0JsSVFBQUFBJCQAAAAAAAAAAAEAAAABoTqXNTW6x7rHzabU2gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFvXOGVb1zhlZ0; Hm_lvt_e3eec7019ba4d61b236c8afa00fd2ca4=1696254346,1698592096,1698648135; SECKEY_ABVK=Vq5sqWvL9/KRFSHkrXmVh2arr/08mRgAUJL60xiOOTMtDaUJ/llhBnM3FDclVf6xO+tPYLeOhxV1NF1fBGQxKQ%3D%3D; Hm_lpvt_e3eec7019ba4d61b236c8afa00fd2ca4=1698649835; ab_sr=1.0.1_OTFlZDhkNWU5MmIyZTBhNTI5MTZiNmY5MGEzYWUwMTA2OThiYjkyZWRhNTFlNmQ1N2Q4MTU2ZDFmMWU3MGM1YzBkM2ViNmQ1YjAzNzY3ZTVkZmZmNDA2ZjdkNjJiYzYwZWU4MDMxNjU5ZDYwZWFmZGQzYWEyZThlMzMxZWFhZjQ3ZjkyYTkzMDYyMmExYWRjZWRiYzUyMTZjZWRlYzM2ODMyMGI0NTNhMTlmNDY4ZDY5NGE3MGU0NDQ4OWZjY2M5; BMAP_SECKEY=jxxImVi5nZOFLBbqjTfHHqjF2Xej5X-sZYUCzoonbSYqkAvDhVHX_xQtoAgBZP--8ypnbV2L4EIFBpqzs56nQ6opZ9miYxEjX5A7A6peI2ZWvDfd9Ktj-flWUUMz2QrU5EG_CvpMzC_v4o0LNLZF4gPGtMMpYhnk_zpGkJHEtNrpqoZeaTog6mXL_ajlM1ws',
    'pragma': 'no-cache',
    'referer': 'https://zhaopin.baidu.com/quanzhi?query=%E5%BC%80%E5%8F%91',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
}

params = {
    'query': '开发',
}

response = requests.get('https://zhaopin.baidu.com/quanzhi', params=params, cookies=cookies,headers=headers).text
# print(response)
nekot = re.search(r'data\["nekot"\] = "(.*?)";',response).group(1)
print(nekot)
token = nekot[::-1]
print(token)



# 设置每页的条目数
page_size = 50

# 循环遍历多个页面
for page_number in range(0, 1000, page_size):  # 假设要爬取前100页，可根据需要修改上限
    params = {
        'query': '开发',
        'city': '北京',
        'is_adq': '1',
        'pcmod': '1',
        'token': token,
        'pn': str(page_number),
        'rn': str(page_size),
    }
    res = requests.get('https://zhaopin.baidu.com/api/qzasync', params=params, cookies=cookies, headers=headers).json()
    # print(res)
    disp_data = res['data']['disp_data']
    # print(disp_data)
    for item in disp_data:
        job_name = item['title']
        salary = item['ori_salary']
        job_column = item['jobfirstclass'] # 工作类别
        location = item['location'] #  工作地点
        education = item['education'] # 教育程度
        company_name = item['company'] #
        provider = item['provider'] # 来源
        experience = item['experience'] # 经验
        lastmod = item['lastmod']  # 发布时间
        print(job_name,salary,job_column,job_column,location,education,company_name,provider,experience,lastmod)

        # 插入数据到数据库表
        insert_query = "INSERT INTO baidu_job (job_name, salary, job_column, location, education, company_name, provider, experience, lastmod) VALUES (%s, %s,%s, %s, %s, %s,%s, %s,%s)"
        data_tuple = (job_name, salary, job_column, location, education, company_name, provider, experience, lastmod)

        cursor.execute(insert_query, data_tuple)

# 提交更改并关闭数据库连接
db.commit()
db.close()


