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
encrypt_text = "izT9H9OVlWUQbcaffJC0a0eUX/2LzLo+RaFcweMkMiTPbYEZypMHlDitDGeTrDgM8g5t9uXvP/HlBWJJfQmMVdb7qDroTMiiIRflyDngH0lzXptAjTy0H+C1Hzpd8BpHZ72zQ/K/fJrBnLv6iYmYnwRwn72rUBHDTAMsdIjxxm4="
with open("client-private.pem") as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(encrypt_text), sentinel=b'decrypt error')
    print(text.decode('utf-8'))
