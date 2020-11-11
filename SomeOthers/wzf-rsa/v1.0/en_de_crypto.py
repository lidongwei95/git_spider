"""
=========================
# @Time : 2020/11/11 下午1:58
# @Author : ldw
# @File : en_de_code_rsa
# @Software: PyCharm
===========================
"""
from rsa_util import RsaUtil
import os
import base64
import requests
import time


"""输入数据"""
# data = """java函数，模拟获取数据”“”
response = requests.get(url="https://www.baidu.com")
data = response.content.decode("utf-8")

#----------模拟接口得到的base64加密数据-------------
data = "for example"
data = base64.b64encode(data.encode("utf-8"))
#--------------end-----------------------------

# 解密 api data
data = base64.b64decode(data).decode("utf-8")
data = data + "key" + "sysid" + str(time.time())

# 以下3行md5加密不清楚
# m = hashlib.md5()
# m.update(data.encode(charset))
# h = m.hexdigest().encode(charset)
#data = "{\"0\":\"0\",\"1\":\"1\",\"10\":\"10\",\"11\":\"11\",\"12\":\"12\",\"13\":\"13\",\"14\":\"14\",\"15\":\"15\",\"16\":\"16\",\"17\":\"17\",\"18\":\"18\",\"19\":\"19\",\"2\":\"2\",\"3\":\"3\",\"4\":\"4\",\"5\":\"5\",\"6\":\"6\",\"7\":\"7\",\"8\":\"8\",\"9\":\"9\"}"

"""生成证书的存放路径"""
path = "xxxxx"
with open(path + "/client-public.pem") as f_pub_en:
    pub_key = f_pub_en.read()
    print(pub_key)
with open(path + "/client-private.pem") as f_pri_de:
    pri_key = f_pri_de.read()
    print(pri_key)

rsa_util = RsaUtil(pub_key, pri_key)
print('原文: {}'.format(data))

def encrypt_msg():
    """加密结果
    1.进行RSA加密
    2.将加密结果转为16进制字符串
    3.将所有字母大写
    """
    encrypt_ = rsa_util.public_long_encrypt(data)
    encrypt = encrypt_.hex().upper()
    print('加密: {}'.format(encrypt))
    return encrypt

def decrypt_msg(encrypt):
    """解密结果
    1.加密方式逆推解密
    """
    decrypt_str = rsa_util.private_long_decrypt(bytes.fromhex(encrypt.lower()))
    print('解密: {}'.format(decrypt_str))
    return decrypt_str

def sign_msg():
    """签名结果"""
    sign = rsa_util.sign(data)
    print('sign: {}'.format(sign))
    return sign

def verify_sign(decrypt_str,sign):
    """验签结果"""
    verify = rsa_util.verify(decrypt_str, sign)
    print('verify: {}'.format(verify))
    return verify

encrypt = encrypt_msg()
decrypt_str = decrypt_msg(encrypt)
sign = sign_msg()
verify_sign(decrypt_str,sign)
