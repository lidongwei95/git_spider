import socket
import time

def main():
    s = socket.socket()

    s.bind(("",8081)) # 绑定地址和端口
    #Symbolic name meaning all available interfaces
    s.listen(5)       # 等待客户端连接，连接数为参数
    while(True):
        c,addr = s.accept()         # 建立客户端连接    
        print("与"+str(addr)+"建立了连接")

        index = 0
        while(index<10):
            now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            c.send(now_time.encode("utf-8"))
            time.sleep(10)
            index = index + 1 
            c.close()   


if __name__ == "__main__":
    main()
