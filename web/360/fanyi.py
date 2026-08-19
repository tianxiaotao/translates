#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/6 14:00
# @Author : Carey
# @Description

import requests

url = 'https://fanyi.so.com/index/search?eng=1&validate=&ignore_trans=0&query=trans'
headers = {
'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
'Host': 'fanyi.so.com',
'Origin': 'https://fanyi.so.com',
'Pragma': 'no-cache',
'pro': 'fanyi',
'Referer': 'https://fanyi.so.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}
# 长度有限
text = '你好帅哥'
data = {
    'eng': '0',
    'validate':'',
    'ignore_trans': 0,
    'query': text
}
response = requests.post( url, headers=headers, data=data )
print( f"{response.json()['msg']} ===> {response.json()['data']['fanyi']}"  )