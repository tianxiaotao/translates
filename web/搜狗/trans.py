#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/15 9:18
# @Author : Carey
# @File : trans.py
# @Description
import json
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import requests
import execjs

headerInfo = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

req = requests.get( 'https://fanyi.sogou.com/text', headers=headerInfo )
strCookie = ''
for k,v in req.cookies.get_dict().items():
    strCookie += f'{k}={v}; '

del req
del headerInfo

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://fanyi.sogou.com',
    'Referer': 'https://fanyi.sogou.com/text',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cookie': strCookie,
}

js_file = "trans.js"
with open(js_file, "r", encoding='utf8')as f:
    js_tamp = f.read()


trans = '你好'
to = 'en'

jsDrive = execjs.compile( js_tamp )
arrInfo = jsDrive.call( 'getEnc', to,  trans )

json_data = {
    'from': 'auto',
    'to': 'en',
    'text': trans,
    'client': 'pc',
    'fr': 'browser_pc',
    'needQc': 1,
    's': arrInfo[ 's' ],
    'uuid': arrInfo[ 'uid' ],
    'exchange': False,
}

response = requests.post( 'https://fanyi.sogou.com/api/transpc/text/result', headers=headers, json=json_data )
print( response.cookies.get_dict() )
print( response.text )
