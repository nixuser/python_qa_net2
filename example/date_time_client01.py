import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("localhost", 40404))
data = ''
one_byte = s.recv(1)
while one_byte:
    data += one_byte.decode()
    one_byte = s.recv(1)
s.close()
print(data)
