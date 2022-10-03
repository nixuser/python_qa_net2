import socket

def receive_data_stream(socket):
    data = ''
    while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            packet = socket.recv(1024)
            if not packet:
                # if data is not received break
                break
            data += packet.decode()
    return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   # now connect to the server on port 40404
    s.connect(("localhost", 40404))
    time_and_date = receive_data_stream(s)
print(time_and_date)
