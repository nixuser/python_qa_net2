import socket

from demo.config import LOCALHOST

my_socket = socket.socket()
# Define this port
TARGET_PORT = None
address_and_port = (LOCALHOST, TARGET_PORT)

# https://docs.python.org/3/library/socket.html#socket.socket.connect
my_socket.connect(address_and_port)
my_socket.close()
