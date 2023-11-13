import re
import requests
import time


def get_comments(url, headers, cookies):
    while url:
        response = requests.get(url, headers=headers, cookies=cookies).json()

        # 处理当前页的评论
        process_comments(response)

        # 获取下一页的参数
        next_page = response['paging']['next']
        offset = re.search(r'offset=(\d+)', next_page).group(1)

        # 构建下一页的URL
        url = re.sub(r'offset=\d+', f'offset={offset}', url)

        # 为了防止频繁请求，添加延迟
        time.sleep(1)


def process_comments(response):
    data = response.get('data', [])
    for comment in data:
        content = comment.get('content', '')
        like_count = comment.get('like_count', 0)
        author = comment.get('author', {}).get('name', '')
        print("评论:", content, "点赞量:", like_count, "用户名:", author)

        # 处理子评论
        child_comments = comment.get('child_comments', [])
        for child_comment in child_comments:
            reply = child_comment.get('content', '')
            print("回复:", reply)

        print("=============================================")


# 初始URL，第一页的评论
initial_url = 'https://www.zhihu.com/api/v4/comment_v5/answers/1514657575/root_comment?order_by=score&limit=20&offset='

headers = {
    # ... 你的其他请求头 ...
    'x-zse-96': '2.0_...',  # 你的 x-zse-96 参数
}

cookies = {
    # ... 你的其他 cookie ...
}

get_comments(initial_url, headers, cookies)
