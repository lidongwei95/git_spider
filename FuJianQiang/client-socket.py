import socket
  
s = socket.socket()

s.connect(("10.0.93.39",9000))
while True:
    print (s.recv(1024))
    s.close()

