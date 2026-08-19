#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/4/22 18:38
# @Author : Carey
# @File : translation.py
# @Description
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import time
import json
import requests
import execjs

iTime = round( time.time()*1000 )

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=2832382@117.22.144.72; OUTFOX_SEARCH_USER_ID_NCOO=1947820840.9198918; DICT_DOCTRANS_SESSION_ID=YWRiYTJjYmUtNmMwZC00MTA4LTgyMWItOTBmMDQ5MzUzZmI2'
}


def getSign( param, key ):
    """
    获取加密参数 sign
    """
    with open( 'translation.js', 'r', encoding='utf-8', errors='ignore' ) as f:
        js_tamp = f.read()
    jsDrive = execjs.compile( js_tamp )
    data = {
        'client': param[ 'client'] ,
        'time': iTime,
        'product': param[ 'product' ],
        'key': key
    }
    sign = jsDrive.call( 'getSign', data )
    return sign

def getAesInfo():
    """
    获取加密key及解密key与iv数据
    """
    query = {
        'keyid': 'webfanyi-key-getter',
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': iTime,
        'keyfrom': 'fanyi.web',
        'mid': 1,
        'screen': 1,
        'model': 1,
        'network': 'wifi',
        'abtest': 0,
        'yduuid': '2f9fca73d004ffed88121a15b5e4b717'
    }
    key = 'asdjnjfenknafdfsdfsd'
    query[ 'sign']  = getSign( query, key )
    response = requests.get( 'https://dict.youdao.com/webtranslate/key', headers=headers, params=query )
    if response.status_code == 200:
        result = json.loads( response.text )
        return { 'key': result['data']['secretKey'], 'aesKey': result['data']['aesKey'], 'aesIv': result['data']['aesIv'] }
    else:
        print( response )
        print( response.text )


def getTranslation( trans, keyInfo ):
    """
    请求翻译接口并对结果解密
    """
    data = {
        'i': trans,
        'from': 'auto',
        'to': '',
        'domain': 0,
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': iTime,
        'keyfrom': 'fanyi.web',
        'mid': 1,
        'screen': 1,
        'model': 1,
        'network': 'wifi',
        'abtest': 0,
        'yduuid': '2f9fca73d004ffed88121a15b5e4b717',
    }
    data['sign'] = getSign( data, keyInfo['key'] )

    response = requests.post('https://dict.youdao.com/webtranslate', headers=headers, data=data )
    if response.status_code == 200:
        with open( 'translation.js', 'r', encoding='utf-8', errors='ignore' ) as f:
            js_tamp = f.read()
        jsDrive = execjs.compile(js_tamp)

        arg = {
            't': keyInfo['aesKey'],
            'n': keyInfo['aesIv']
        }
        info = jsDrive.call('aesDecrypt', response.text, arg )
        print( arg )
        print( info )
    else:
        print( response )
        print( response.text )



if __name__ == '__main__':
    keyInfo = getAesInfo()
    getTranslation( '你叫什么名字', keyInfo )