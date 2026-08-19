#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/7/26 18:09
# @Author : Carey
# @File : index.py
# @Description
import re

import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://fanyi.baidu.com/mtpe-individual/multimodal',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'smallFlowVersion=old; BAIDUID=9320FAA11E71A6E98AD195DB3C6062F4; BAIDUID_BFESS=9320FAA11E71A6E98AD195DB3C6062F4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
}

response = requests.get('https://fanyi.baidu.com/', headers=headers)
response.encoding = 'utf-8'
print( response )

print( response.cookies.get_dict() )

token = re.findall( r'token:(?:\s+)\'(.*?)\'', response.text.strip(), re.S )
print( token[0] )
