import socket

HOST = socket.gethostname()
PORT = 8889

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:

        conn.send("Hello, I am server!".encode("utf-8"))

        while True:
            data = conn.recv(1024)
            print("Recieved", data, "from", addr)

            if not data:
                print("Got", data, "and closed connection")
                break

            data = data.decode("utf-8")[::-1]

            conn.send(data.encode("utf-8"))
            print("Send", data, "to", addr)
