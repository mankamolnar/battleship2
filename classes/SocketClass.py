import socket
from classes.model.SocketAbstract import SocketAbstract, ClientSocketAbstract, ServerSocketAbstract


class Socket(SocketAbstract):

    # defining that you are the host or the client
    def __init__(self):
        self.HOST = "127.0.1.1"
        self.PORT = 9999
        self.s = socket.socket()
        self.started = False

    # closing the socket
    def closeSocket(self):
        self.s.close()


class ClientSocket(ClientSocketAbstract, Socket):

    # start client socket
    def startSocket(self):
        print("Connecting to server...")
        self.s.connect((self.HOST, self.PORT))

    # Receive on server side
    def receiveData(self):
        data = self.s.recv(1024)
        return data.decode("utf-8")

    # send data as a client
    def sendData(self, data):
        self.s.send(str.encode(data))


class ServerSocket(ServerSocketAbstract, Socket):

    # construct changes. We have conn, and addr here
    def __init__(self):
        self.HOST = "127.0.1.1"
        self.PORT = 9999
        self.s = socket.socket()
        self.conn = ""
        self.connAddr = ""
        self.started = False

    # start server socket
    def startSocket(self):
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(1)
        print("Waiting to connect by someone...")
        self.conn, self.connAddr = self.s.accept()
        self.started = True

    # Receive on client side
    def receiveData(self):
        data = self.conn.recv(1024)
        return data.decode("utf-8")

    # send data as a server
    def sendData(self, data):
        self.conn.send(str.encode(data))