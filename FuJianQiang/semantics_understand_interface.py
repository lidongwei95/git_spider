#!/usr/bin/python3
#*-*coding=utf-8 *-*
import requests
"""重要内容，切勿上传"""

def get_semantic():
    json_params = {
    "query":"查一下明天从北京到上海的南航机票",
    "city":"北京",
    "category": "flight,hotel",
    "appid":"wx729238547ac7a14c",
    "uid":"five_love_forever"
    }

    url = "https://api.weixin.qq.com/semantic/semproxy/search?access_token="
    resp = requests.post(url, json_params)
    print(resp.text)


"""
http请求方式: POST（请使用https协议）

https://api.weixin.qq.com/semantic/semproxy/search?access_token=YOUR_ACCESS_TOKEN

POST数据格式：JSON

POST数据例子：

{
"query":"查一下明天从北京到上海的南航机票",
"city":"北京",
"category": "flight,hotel",
"appid":"wxaaaaaaaaaaaaaaaa",
"uid":"123456"
}
wx729238547ac7a14c 中国南方航空
wxa32eb3d60a0e6278 阴阳典当行
APPSECRET  6925c2e856410163817792bb623507cc
"""
def get_access_token():
    # url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET"
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % ("wxa32eb3d60a0e6278", "6925c2e856410163817792bb623507cc")
    access_token = requests.post(url)
    print(access_token.text)

get_access_token()