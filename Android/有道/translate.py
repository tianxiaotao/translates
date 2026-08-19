#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2024/12/10 15:08
# @Author : Carey
# @File : translate.py
# @Description

import requests
import hashlib
import time


headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Host': 'dict.youdao.com',
    'User-Agent': 'okhttp/5.0.0-alpha.14',
}

data = 'dicts={"count":73,"dicts":[["ct"],["tc"],["ec"],["ce"],["newjc"],["newcj"],["yd_cj"],["yd_jc"],["newcj_sents"],["jtj"],["ck"],["kc"],["cf"],["fc"],["multle"],["longman"],["newcenturyfc"],["collins"],["ec21"],["exam_dict"],["ee"],["hh"],["newhh"],["ce_new"],["special"],["web_trans"],["pic_dict"],["word_video"],["rel_word"],["phrs"],["syno"],["wordform"],["ywAncientWord"],["ywBasic"],["ywRelatedWords"],["ywWordNet"],["ywIdiom"],["ywSynAndAnt"],["blng_sents_part"],["auth_sents_part"],["media_sents_part"],["baike"],["etym"],["wikipedia_digest"],["typos"],["web_search"],["fanyi"],["tcb"],["ctc"],["ugc"],["oxfordAdvance"],["huge_ec"],["huge_ce"],["newcenturyjc"],["oxford"],["webster"],["special_economy"],["special_medicine"],["special_elec_commu_auto_control"],["special_mechanical"],["special_energy"],["special_biology"],["special_traffic"],["special_computer"],["special_other"],["video_sents"],["longchao-ck"],["longchao-kc"],["individual"],["expand_ec"],["ja_exam_sents"],["music_sents"],["wordElaboration"]]}'


iTime = int( time.time() * 1000 )

params = {
    "q": "你是谁啊！",
    "le": "",
    "t": str(iTime),
    "client": "mobile",
    "jsonversion": "4",
    "keyversion": "20171115",
    "product": "mdict",
    "appVersion": "10.1.14",
    "keyfrom": "mdict.10.1.14.android",
    "network": "wifi",
    "vendor": "youdaoweb",
}


def getSign( params ):
    strShort = hashlib.md5( params['keyfrom'].encode( 'UTF-8' ) ).hexdigest()

    strEnc = f"{params['client']}{params['q']}{params['t']}ydsecret://query.token/signkey/ioHOsiqdVRrm@T!h!b9@pBf&YrE5FPe0I7qAup6WL^9AV16J4J{strShort}"
    return hashlib.md5( strEnc.encode( 'UTF-8' ) ).hexdigest()


sign = getSign( params )
params[ 'sign' ] = sign


response = requests.post( 'https://dict.youdao.com/jsonapi_s', headers=headers, params=params, data=data )

print( response )
print( response.text )