import socket
moj_socket = socket.socket()

moj_socket.bind(("0.0.0.0", 4445))
moj_socket.listen(1)
conn,addr = moj_socket.accept()

moj_socket.close()