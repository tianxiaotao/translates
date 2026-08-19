#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/12/10 10:28
# @Author : Carey
# @File : translate.py
# @Description

import requests
import hashlib
import time

headers = {
    'User-Agent': 'BDTApp; Android 9; BaiduTranslate/11.8.0',
    'Host': 'fanyi-app.baidu.com',
    'Content-Type': 'application/x-www-form-urlencoded',
}

params = {
    'product': 'transapp',
    'appVersion': '11.8.0',
    'cuid': '9C172D564BC0C22860DE3FE250241C4D|VQWMC57B7',
    'channel': 'PC',
    'type': 'json',
    'version': '186',
    'systemVersion': '9',
    'appNick': '',
    'syslan': 'zh',
    'trans_mode': '3',
    'appUserTags': '{"key1":["1100"]}',
    'netterm': 'WIFI',
    'vendor': 'Google Phone',
    'sysmodel': 'Google Phone_G576D',
    'os_lang': 'zh',
    'dvh': '1280',
    'plat': 'android',
    'req': 'v2trans',
}

iTime = int( time.time() * 1000 )

data = {
    'firstVersionTime': '1733797299636',
    'isnew': '0',
    'loginTime': '0',
    'trans_page_from': 'page_home_trans_result',
    'zhType': '0',
    'from': 'auto',
    'timestamp': str(iTime),
    'user_status': '0',
    'query': '你是谁',
    'needfixl': '1',
    'isnewDevice': '0',
    'lfixver': '1',
    'is_show_ad': '1',
    'appRecommendSwitch': '1',
    'deviceModel': 'Android_Pad',
    'to': 'en',
    'page': 'translate',
}

def getSign( params, data ):
    data.update( params )
    keys = sorted( data.keys() )

    arrMd5Enc = []
    for key in keys:
        arrMd5Enc.append( f'{key}{data[key]}' )

    strShortMd5 = f"0{params['cuid']}{params['appVersion']}607e34f0fb3bf7895c102dacf9e9b0d7{data['timestamp']}"
    short = hashlib.md5(strShortMd5.encode(encoding='UTF-8')).hexdigest()
    arrMd5Enc.append( short )

    strMd5Enc = "".join( arrMd5Enc )
    return hashlib.md5(strMd5Enc.encode(encoding='UTF-8')).hexdigest()


sign = getSign( params, data )
data[ 'sign' ] = sign

response = requests.post( 'https://fanyi-app.baidu.com/transapp/agent.php', params=params, headers=headers, data=data )
print( response )
print( response.text )