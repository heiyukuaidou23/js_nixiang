import subprocess

import execjs
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/xml;charset=UTF-8',
    'Origin': 'http://www.ccprec.com',
    'Pragma': 'no-cache',
    'Referer': 'http://www.ccprec.com/navCqzr/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
}
# 运行JavaScript文件作为子进程
process = subprocess.Popen(['node', './jilin_jiaoyi.js'], stdout=subprocess.PIPE, text=True)

# 从子进程的标准输出中获取生成的密钥
data1, _ = process.communicate()
# data_list = data.split(',')
print(data1)
# data = '005tnlk8cewrda6vqeosnx9yut4n5v6t4b6v5u6m627c7n597z7a7m835n5y844v76657u595w727d4z6d968p9c6b724r8k7c8p7s7j6i9q649d9d704t755g5s5v68696a816l5g539r8c849886978i5180925m606f5i68617g6k837s5p6b4b7l95848p7e948r5p8k9p8i6g8w7x946m7a7g8i5k7c62406j7m746u7z7o6957667f956m8a7k976f6x8d7p6o6v6x52826p576e7i5g7t4h808c93648q9n736p865k7l977v8d609c6y5n757l6h6y606k84713u6a6u7k7q7873887a7c7a5u7f6f6n7k7v8z8l585w7q7v3u6n7r7r6s8v7s9r8c61786v7n9l67798a8u7g5s8j716i52635g7f5n675u8776566d6q6c6r7e7y9c887w4g7a6h7c4c5x6h73647b757l6w615l4s786s6m7i8z6v665n7r6o6u69697v6s3y5z6n7u9h725r6d7s928d7v8v818c4i7i7o8k4w617v6s4b6c7e6d6v7u5w6a6m7c7w8j7k8d7j6a847d7s617e75695e575p836g6l5l5t8t79849m81817t6i9u885v618k5n9d5v6y5z95998f8t7b8e6o757k8y8e725u9i9c7e6d92838a7t81938m767d8a699j5o5r6t7b7j7g64756m7b3w5v7b7x75749074606u734x6w7y607y6z5t6e5f627k7s667x93735r7y6l6q7a585l6b6k7367747d5t'

response = requests.post('http://www.ccprec.com/honsanCloudAct', headers=headers, data=data1).text
print(response)