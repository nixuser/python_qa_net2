import socket

from demo.config import LOCALHOST

# Define this target port
TARGET_PORT = None

my_socket = socket.socket()
address_and_port = (LOCALHOST, TARGET_PORT)

my_socket.connect(address_and_port)

# https://docs.python.org/3/library/socket.html#socket.socket.send
data_amount = my_socket.send(b"Hello, socket!")
print("Send", data_amount, "bytes")

my_socket.close()
