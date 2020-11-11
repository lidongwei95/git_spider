"""
=========================
# @Time : 2020/11/11 下午1:15 
# @Author : ldw
# @File : decode_rsa
# @Software: PyCharm
===========================
"""
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
encrypt_text ="S1NckUAKDrp1+5qtoq4fesaGZrP/RGnwizvtxRoQ6cYi6do5vHH/1l6mg3MuasJinatNYpErJvCX1NyDjM088W6tzmksDLoikt2ZGakvF9lmo12rrG4ENERZOoN8SgjGQi3G+C4jwOa+3Lc0NYPjday/aCn9iOLTee738weHyfVOz/J6YkTqRoVUZ3kOODjiLTugSX0oSEzqSGi2VZ2OsTpAeSwiG9eztpGO3Z6ix3yKDu7yZplUlKXnK0jyUrXeiUF+gbDSrxPbw8uHzraRQRv5XsvbDPQGvKn6vLZR3jQiiFFbJ+Vk3gDy3HbRyXH/fFd471u9/1cso2BTdi6iJQ==" 
with open("client-private.pem") as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(encrypt_text), sentinel=b'decrypt error')
    print(text.decode('utf-8'))
