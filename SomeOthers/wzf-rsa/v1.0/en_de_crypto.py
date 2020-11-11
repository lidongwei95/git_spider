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

"""输入数据"""
# data = """借口函数，获取到需加密的内容”“”
data = "{\"0\":\"0\",\"1\":\"1\",\"10\":\"10\",\"11\":\"11\",\"12\":\"12\",\"13\":\"13\",\"14\":\"14\",\"15\":\"15\",\"16\":\"16\",\"17\":\"17\",\"18\":\"18\",\"19\":\"19\",\"2\":\"2\",\"3\":\"3\",\"4\":\"4\",\"5\":\"5\",\"6\":\"6\",\"7\":\"7\",\"8\":\"8\",\"9\":\"9\"}"

"""生成证书的存放路径"""
path = "xxx"
with open(path + "/client-public.pem") as f_pub_en:
    pub_key = f_pub_en.read()
    print(pub_key)
with open(path + "/client-private.pem") as f_pri_de:
    pri_key = f_pri_de.read()
    print(pri_key)

rsa_util = RsaUtil(pub_key, pri_key)
print('原文: {}'.format(data))

"""加密结果"""
encrypt = rsa_util.public_long_encrypt(data)
print('加密: {}'.format(encrypt))

"""解密结果"""
decrypt_str = rsa_util.private_long_decrypt(encrypt)
print('解密: {}'.format(decrypt_str))

"""签名结果"""
sign = rsa_util.sign(data)
print('sign: {}'.format(sign))

"""验签结果"""
verify = rsa_util.verify(decrypt_str, sign)
print('verify: {}'.format(verify))
