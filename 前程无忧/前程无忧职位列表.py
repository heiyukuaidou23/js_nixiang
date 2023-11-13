import csv
import time

import execjs
import requests
import uuid
from datetime import datetime

# 获取当前时间
current_time = datetime.now()

# 将当前时间转换为精确到毫秒的时间戳
timestamp = int(current_time.timestamp() * 1000)

print(timestamp)
cookies = {
    'guid': '313611d42d909d6fb03ee65cc6cb1668',
    'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
    'Hm_lvt_1370a11171bd6f2d9b1fe98951541941': '1699518301,1699551790',
    'acw_sc__v3': '654d1d0bcc02d3054e38ed8bf579b191f240c207',
    'ps': 'needv%3D0',
    '51job': 'cuid%3D227188604%26%7C%26cusername%3D6EkqE5F1hletXXUGJwztWHBiiG8tfvVOwkiwgQ8G%252BtE%253D%26%7C%26cpassword%3D%26%7C%26cname%3DRy7tMOA1jlburp6HnwL71A%253D%253D%26%7C%26cemail%3Dhhs8QYaYftgqZ%252ByMaLlFZ7sdL%252FNyE5dGL0QyhaBbXV4%253D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0buwSGCZ6YIc%26%7C%26cconfirmkey%3DzhfqeqzveKWew%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3Dzhv87FK7s4ins%26%7C%26to%3D91e42f9a1af0c085f49fd391c8a4116f654d1dea%26%7C%26',
    'sensor': 'createDate%3D2023-05-16%26%7C%26identityType%3D2',
    'acw_tc': 'ac11000116995527471445297e00d82f89a9d507e9a3b77354266dfeeaf04c',
    'slife': 'lowbrowser%3Dnot%26%7C%26lastlogindate%3D20231110%26%7C%26securetime%3DBjpcaVI9Uj8HYAE6X2ZcMFNkBjY%253D',
    'acw_sc__v2': '654d1decb8a2805d0a1a851054440a1bb8e5b1ed',
    'partner': 'cn_bing_com',
    'seo_refer_info_2023': '%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fcn.bing.com%5C%2F%22%2C%22referHost%22%3A%22cn.bing.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D',
    'privacy': '1699552822',
    'Hm_lpvt_1370a11171bd6f2d9b1fe98951541941': '1699552825',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22227188604%22%2C%22first_id%22%3A%2218a78ec7ef512c9-02dc525034d0bba-7f5d547e-1327104-18a78ec7ef61193%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhNzhlYzdlZjUxMmM5LTAyZGM1MjUwMzRkMGJiYS03ZjVkNTQ3ZS0xMzI3MTA0LTE4YTc4ZWM3ZWY2MTE5MyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjIyNzE4ODYwNCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22227188604%22%7D%2C%22%24device_id%22%3A%2218a78ec7ef512c9-02dc525034d0bba-7f5d547e-1327104-18a78ec7ef61193%22%7D',
    'search': 'jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B8%D5%B9%FB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B8%D5%B9%FB%A1%FB%A1%FA1%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B8%D5%B9%FB%B2%C9%BF%F3%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BF%E7%BE%B3%B5%E7%C9%CC%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
    'JSESSIONID': '915F8CC534AA50FD79D5D6C237135347',
    'ssxmod_itna': 'eqAhiKDK0KzGODzrK224mqKWu/GxUoOdxQ4D5bdD/K9+DnqD=GFDK40EY8+umYP5Y14n3bbCZ72fTdYn8wRaG9lQ2fsaDCPGnDB9wqFeqYYCDt4DTD34DYDix5DLDmeD+ATKDd6vsNskvxiOD7eDXxGCDQIGx4DaDGakHi4CoDDzoAO4qiAKDmbk92P+4fYDnZG1qQikD75Dux0HkYk46xDCuFk4lOvfj/g3vOAhDCKDjcY1zEYDUDvsBr9vDZnxee2N5CbeknRqqC4KemGbOyDY7q4K574LkGhIkBbyamp9DDcDCS6P4D==',
    'ssxmod_itna2': 'eqAhiKDK0KzGODzrK224mqKWu/GxUoOdxQ4D5bG9WNztxBMoge7p5jIk05zBm8D8O06s4ob0B085G6e7QGd5AmBwfcFGpfW+G0z6kr2=P5ZYTjoo4md8yTqwtE7Q7dw/L7gxxakG1+xy45CqCiByoSomsHCvbel5zxPgOd=Ea3ZGm7OOhzFqY2lnstrnbnZH86p9Wcm8kIFqiBaBKKreaHIpje1dLUhWX6IMLKaYzDp3rBoQE=HfL0RdLRpdnSRFrUfPi6pGj35tcfzdEHr8bmF0BiNf9ONL2jfcg6Njg0NzZSH6TPKdbpNacmGWYvajXlj2PQw6iFai6Ei6Zd4ttnxXBretA4DQ9Q00o+2QzPiz0oXr44gYr+orgDAxQGoTFGsSxxD+YFGFKDufgt0gsKiQSg=9imi04/uKUDDFqD+pDxD=',
}

with open('job.csv', 'a', newline='', encoding='utf-8') as csvfile:
    # 创建CSV写入器对象
    csvwriter = csv.writer(csvfile)

    # 写入标题行
    csvwriter.writerow(['职位名称', '职位标签', '工作地区', '薪资', '公司名称', '公司规模', '工作类型'])
# 随机生成UUID对象
    uuid_obj = uuid.uuid4()
    for pageNum in range(1,33):
        e = f"/api/job/search-pc?api_key=51job&timestamp={timestamp}&keyword=%E5%88%9A%E6%9E%9C&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={pageNum}&requestId=5c73dae885119cdb216bed2883bcc52d&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb"

        sign = execjs.compile(open('./参数加密sign.js', 'r', encoding='utf-8').read()).call('main123',e)
        print(sign)
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'guid=313611d42d909d6fb03ee65cc6cb1668; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; slife=lowbrowser%3Dnot%26%7C%26; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22313611d42d909d6fb03ee65cc6cb1668%22%2C%22first_id%22%3A%2218a78ec7ef512c9-02dc525034d0bba-7f5d547e-1327104-18a78ec7ef61193%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhNzhlYzdlZjUxMmM5LTAyZGM1MjUwMzRkMGJiYS03ZjVkNTQ3ZS0xMzI3MTA0LTE4YTc4ZWM3ZWY2MTE5MyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjMxMzYxMWQ0MmQ5MDlkNmZiMDNlZTY1Y2M2Y2IxNjY4In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22313611d42d909d6fb03ee65cc6cb1668%22%7D%2C%22%24device_id%22%3A%2218a78ec7ef512c9-02dc525034d0bba-7f5d547e-1327104-18a78ec7ef61193%22%7D; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%BF%E7%BE%B3%B5%E7%C9%CC%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%BF%AA%B7%A2%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1699518301; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1699518422; acw_tc=ac11000116995193241816838e00e08475552d09ac50c8ce1669827967454e; acw_sc__v2=654c9b5cffb322b0e2fd5b34b1e0c7f1f0611f2f; JSESSIONID=822AAE0BF71D434E9C80F0BED16EB0A1; ssxmod_itna=Wq0xuDnGiQit0=D7Dz2IdG=697ZDRj7YZ=hPh7Cx0yR0eGzDAxn40iDt=rwiiZPguGYezj8A3HK0j+DKe6KjCcwxiwjSyeDHxY=DUOAn+bD445GwD0eG+DD4DW0x03DoxGASpx0+kSBcu=nDAQDQ4GyDitDKkixxG3D0R6QK3UYDDXY9Q+P3CqDb26MS32xHeDSQBUPF0=DjqGgDBLxI=4yDDt86=+/UkcFx1PntliDtqD9CjUXFeDH+MXl3qno/D3jvB54I7GFQ7x48DhYF4xT+DeezAhNzB4H87ut3B4TUN4DG8htwV4xD; ssxmod_itna2=Wq0xuDnGiQit0=D7Dz2IdG=697ZDRj7YZ=hPh7DnIfhrqDssNKDL7GhZWV1KrQ0DQD67kxN+9/WkxreyUpmoRhNH9jBnNbH+GBaIsLPhSRLbN3CY7j5oL9CBhUwUFdrSzosCMl2cKDIZfxql/MqcAL6Vzi0EnkfPyuiRGlYor80eNn2wjQu5EQjxknXdMWUdxecD5jo=P1Lxp1f41c0ni1uo=PWN21nE9lADZwHa5t7/+Pc/DLNaE=HMIINsE+tAXLH6=TWhUpkGc/nzxXFqNuCW2llpPsikXd/XkFnNoinP+G1rkmWWPwO2NwrY1cQQhDaDG2S049R/Br5U2qWDN+iq/GHFDsIBYbxTmDQ+B59DPriqYnY8DVBYNQg5To5deod0oy2Df74KO5o0=ObeGBk0BoyuQ7oNXxrVYO8iTCg5Ir=70tR2D0it5gzYDKABerg/f7bHDHZSpixDFqD+PxxD',
            'From-Domain': '51job_web',
            'Pragma': 'no-cache',
            'Referer': 'https://we.51job.com/pc/search?keyword=%E8%B7%A8%E5%A2%83%E7%94%B5%E5%95%86&searchType=2&sortType=0&metro=',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'account-id': '',
            'partner': '',
            'property': '%7B%22partner%22%3A%22%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3Fkeyword%3D%25E8%25B7%25A8%25E5%25A2%2583%25E7%2594%25B5%25E5%2595%2586%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%2C%22keywordType%22%3A%22%22%7D',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sign': sign,
            'user-token': '',
            'uuid': str(uuid_obj),
        }

        params = {
            'api_key': '51job',
            'timestamp': timestamp,
            'keyword': '采矿',
            'searchType': '2',
            'function': '',
            'industry': '',
            'jobArea': '000000',
            'jobArea2': '',
            'landmark': '',
            'metro': '',
            'salary': '',
            'workYear': '',
            'degree': '',
            'companyType': '',
            'companySize': '',
            'jobType': '',
            'issueDate': '',
            'sortType': '0',
            'pageNum': pageNum,
            'requestId': '5c73dae885119cdb216bed2883bcc52d',
            'pageSize': '20',
            'source': '1',
            'accountId': '',
            'pageCode': 'sou|sou|soulb',
        }

        response = requests.get('https://we.51job.com/api/job/search-pc', params=params, cookies=cookies, headers=headers).json()
        print(response)
        data_list = response['resultbody']['job']['items']
        for data in data_list:
            jobName = data['jobName']
            jobTags = data['jobTags']
            jobAreaString = data['jobAreaString'] # 工作地区
            salary = data['provideSalaryString'] # 薪资
            CompanyName = data['fullCompanyName']
            companysize = data['companySizeString']
            job_type = data['industryType1Str']
            print(jobName, jobTags, CompanyName)
            time.sleep(1)
            csvwriter.writerow([jobName, jobTags, jobAreaString, salary, CompanyName, companysize, job_type])