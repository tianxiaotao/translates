#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/6 14:00
# @Author : Carey
# @Description

import time
import execjs
import requests


trans = input( '请输入要翻译得文案：' )

js_file = "translate.js"
with open(js_file, "r")as f:
    js_tamp = f.read()

jsDrive = execjs.compile( js_tamp )
sign = jsDrive.call( 'a', trans )

data = {
    "from": "zh",
    "to": "en",
    "query": trans,
    "simple_means_flag": 3,
    "sign": sign,
    "token": "ae60ba349c7c990a60fc989c38bb6622",
    "domain": "common",
    "ts": int( time.time() * 1000 )
}

header = {
    "Accept": "*/*",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7",
    "Origin": "https://fanyi.baidu.com",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://fanyi.baidu.com",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "BAIDUID=8E1E0C424E2C6A8EB8C88243D29156EF:FG=1; BAIDUID_BFESS=8E1E0C424E2C6A8EB8C88243D29156EF:FG=1; smallFlowVersion=old; BIDUPSID=714A2E69FF70CB86AD437471D29C0BA0; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITC00H=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'Acs-Token': '1725184851043_1725255370027_ISxHlh4iAujMYlUUviUqlI5d4w9AAFQweOo8aa3kv0PLOE4Oe/giuJoSpQIem7Xj6BCpzVdGGARrl6uw/USUepnMpWJUHpj6yhsYqCuWoRK3YohvTi+Sqcuy2nkox/RoGd3vOljp/BcN54CcX1YhzNeVcPCi94znekWcGUlvWF59YMQje23tGwUKiCOAQ4dG0cByEVtxUt5CCfNhlaqKmM/Bp+0YQDhx0zqGPI8sRA5mWn/aSiR5yIsJfBUi0QjWpdFSY5aIIR4c/wLW25jXYE/7s0j2ovbHiNF/YnpoNkKJMScY7zX6USPst2BNx1zB9PxmwGEv4HNj+LXlancJJfXrgU9rujr3P7Ao9XnI6AynGOGumx8hpMoMS77nhJs02+oMvw2SIZ7Tvz8Js6V3j2DBz0aepNuaZQ4YpWYmRz225Ovm+v7oWjSK2CEV4C4UbWVYqWkvNnDF7JzLg2qi5IpOoWWSL2QFZ6meyDiOWnE='
}
url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

resp = requests.post( url, data = data, headers = header )
print( resp.cookies.get_dict() )

retData =  resp.json()

print( retData[ 'trans_result'][ 'data' ][0] )