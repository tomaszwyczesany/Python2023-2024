import socket

targetip = "10.0.1.66"
targetport = 22

msocket= socket.socket()
msocket.connect((targetip,targetport))
msocket.send("Get Banner\r\n".encode())

mserver = msocket.recv(2048).decode()
print(f"połączono z serwisem\n\n {mserver}")
