#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/3/6 14:00
# @Author : Carey
# @Description


import requests
import execjs


trans = input( '请输入要翻译得文案：' )

js_file = "translate.js"
with open(js_file, "r")as f:
    js_tamp = f.read()

jsDrive = execjs.compile( js_tamp )
sign = jsDrive.call( 'get_trans_sign', trans )

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1 wechatdevtools/1.06.2401020 MicroMessenger/8.0.5 webview/17070355770738727 webdebugger port/39765 token/afc8e8b5ac4eadac5aa64e5aa77e07c2',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BAIDUID=795A1E35B30501910CDC9C7A7B0A852E:FG=1;  BA_HECTOR=82016k80u58l848k9kah2k00oea2ub1iruh6l1t;  BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695',
}

data = {
    'query': trans,
    'from': 'zh',
    'to': 'en',
    'token': 'c7224d9b7d3e40bda79b5813d31473aa',
    'sign': sign,
}
print( data )

response = requests.post('https://fanyi.baidu.com/basetrans', headers=headers, data=data)
print( response.json() )