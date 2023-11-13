import re

import execjs
import requests
from lxml import etree


for page in range(1,10):
    vvv = execjs.compile(open('cookie加密.js', 'r', encoding='utf-8').read()).call('main123')
    v = re.search(r'v=([^;\s]+)', vvv)
    # print(v)
    cook = v.group(1)
    print(cook)
    cookies = {
        'v': cook,
    }
    # print(target_value)
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'v=A-V0pD5v7LQ9FghoJq7U2ZhI9KoaIpmz49Z9COfKoZwr_gvUr3KphHMmjfh0',
        'Pragma': 'no-cache',
        'Referer': 'https://q.10jqka.com.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'hexin-v': cook,
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(
        f'https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{page}/ajax/1/',
        cookies=cookies,
        headers=headers,
    ).text
    # print(response)
    html = etree.HTML(response)
    lis = html.xpath('//tbody/tr')
    for li in lis:
        name = li.xpath('./td[3]/a/text()')
        now_price = li.xpath('./td[4]/text()') #现价
        up_down = li.xpath('./td[5]/text()') # 涨跌幅
        print(name, now_price, up_down)