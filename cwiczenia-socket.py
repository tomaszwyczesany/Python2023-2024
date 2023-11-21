import socket
moj_socket = socket.socket()
moj_socket.connect(("10.0.1.66", 4444))
moj_socket.close()

