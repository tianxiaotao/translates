#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/12/10 15:08
# @Author : Carey
# @File : translate.py
# @Description
import json

import requests
import hashlib
import time
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESUtil():

    def __init__(self, key, mod, iv ):
        self.key = key
        self.mode = mod
        self.iv = iv

    @staticmethod
    def pkcs7_padding(data):
        length = len(data)
        bytes_length = len(bytes(data, encoding='utf-8'))

        # tips：utf-8编码时，英文占1个byte，而中文占3个byte
        padding_size = length if (bytes_length == length) else bytes_length
        padding = AES.block_size - padding_size % AES.block_size

        # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
        padding_text = chr(padding) * padding
        return data + padding_text

    @staticmethod
    def pkcs7_unpadding(padded_data):
        X = padded_data[-1]
        if 1 <= X <= 16:
            plantext = padded_data[:-X]
        else:
            raise Exception('无效的加密信息!')
        return plantext

    def decrypt(self, data):
        key = bytes(self.key, encoding='UTF-8')
        iv = self.iv
        aes = AES.new(key, self.mode, IV=iv )

        decData = aes.decrypt( base64.b64decode( data ) )
        result = self.pkcs7_unpadding( decData )

        return result.decode( 'utf-8' )

    def encrypt(self, data):
        key = bytes(self.key, encoding='UTF-8')
        iv = self.iv
        data_padded = self.pkcs7_padding( data )
        aes = AES.new(key, self.mode, IV=iv )
        encByts = aes.encrypt( bytes( data_padded , encoding='utf-8' ) )
        result = str(base64.b64encode( encByts ), encoding='utf-8')
        return result


headers = {
    'User-Agent': 'Translate-Android; Version:5.2.1;Sat7XHsT26xChyRj5YJeVhNGy+QGQXqVfHLIHweIBw4Q4E4RBBwCz504t5cGovAD;D4DhdnNbABEoMb1oYg4Ybw==;',
    'Content-Type': 'application/json;charset=UTF-8',
}

params = {
    'osVersion': '28',
    'appVersion': '5.2.1',
    'deviceModel': 'Google Phone',
    'os': 'android',
}

iTime = int( time.time() * 1000 )

def getCipherText( word, rel, to ):
    data = {
        'client': '1',
        'fr': 'sogou-new-fanyi-app',
        'from': rel,
        'needQc': 2,
        'pid': 'sogou-dict-fanyiapp',
        'text': word,
        'to': to,
        'uid': '',
        'version': '5.2.1',
        'isReturnPhonetic': 'on',
        'os': 'android',
        'encrpt': 'on',
        'word_group': True,
        'second_query': True,
        'dict': True,
        'isBaike': 'off',
        'furigana': 0,
        'forceFrom': 0,
        'osVersion': '28',
        'appVersion': '5.2.1',
        'deviceModel': 'G576D',
        'manufacture': 'Google Phone',
        'brand': 'Google Phone',
        'os': 'android',
    }

    strEnc = json.dumps( data )

    k = '7c2e52d43aad8720315ab624b9c9fa0f'
    iv = "\0".encode("utf-8") * 16
    aes = AESUtil( k, AES.MODE_CBC, iv )
    return aes.encrypt( strEnc )

def getDecryptText( data ):
    k = 'cf8d51685b1374cb22329bbf0af3905a'
    iv = "\0".encode("utf-8") * 16
    aes = AESUtil(k, AES.MODE_CBC, iv)
    return aes.decrypt( data )

enc = getCipherText( '你好啊', 'zh-CHS', 'en' )

json_data = {
    'cipherText': enc,
    'debug': '0',
}
response = requests.post( 'https://fanyiapp.sogou.com/translateServer/textTranslationV3', params=params, headers=headers,  json=json_data )
print( response )

decData = getDecryptText( response.json()[ 'data' ] )
print( decData )