"""
=========================
# @Time : 2020/11/11 下午1:13 
# @Author : ldw
# @File : encode_rsa
# @Software: PyCharm
===========================
"""
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


def msg_encrypt(message):
    with open("client-public.pem") as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
        print(cipher_text.decode('utf-8'))

#message = "hello client, this is a message"
message = input("enter something need encode:\n")
msg_encrypt(message)
