import socket
import datetime

# Create a TCP server socket
serverSocket = socket.socket();

# Bind the tcp socket to an IP and port
serverSocket.bind(("127.0.0.1", 40404));

# Keep listening
serverSocket.listen();

while(True):
    # Keep accepting connections from clients
    (clientConnection, clientAddress) = serverSocket.accept();

    # Send current server time to the client
    serverTimeNow = "%s"%datetime.datetime.now();
    clientConnection.send(serverTimeNow.encode());
    print("Sent %s to %s"%(serverTimeNow, clientAddress));

    # Close the connection to the client
    clientConnection.close();
