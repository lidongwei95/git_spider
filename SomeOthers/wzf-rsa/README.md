python 处理 RSA加密、解密、签名、验签

一、环境配置
ubuntu16.04
使用python3.5.2

安装环境依赖
## pipreqs . --encoding=utf8 --force // 在项目下打包环境依赖到requirement.txt
python3 -m pip install -r requirements.txt

1、先使用 wzf_rsa.py 生成公钥私钥
2、使用 en_de_crypto.py 调用接口，获取参数，并使用其中的方法实现相应需求

