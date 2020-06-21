import socket

HOST = socket.gethostname()
PORT = 8889

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(repr(data))

    while True:
        data_to_send = input("Let's send:")

        if data_to_send == 'close':
            break

        s.send(bytes(data_to_send.strip(), "utf-8"))
        data = s.recv(1024)

        print('Received', repr(data))
