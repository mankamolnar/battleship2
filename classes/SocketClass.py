import socket
from classes.model.SocketAbstract import SocketAbstract, ClientSocketAbstract, ServerSocketAbstract


class Socket(SocketAbstract):

    # defining that you are the host or the client
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 9999
        self.s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.started = False

    # closing the socket
    def closeSocket(self):
        self.s.close()


class ClientSocket(ClientSocketAbstract, Socket):

    def __init__(self, ip):
        super().__init__()
        self.HOST = ip

    # start client socket
    def startSocket(self):
        try:
            self.s.connect((self.HOST, self.PORT))
        except ConnectionRefusedError:
            self.started = False
        else:
            self.started = True
        return self.started

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
        super().__init__()
        self.conn = ""
        self.connAddr = ""

    # start server socket
    def startSocket(self):
        self.s.bind(('', self.PORT))
        self.s.listen(1)
        self.conn, self.connAddr = self.s.accept()
        self.started = True
        return self.started

    # Receive on client side
    def receiveData(self):
        data = self.conn.recv(1024)
        return data.decode("utf-8")

    # send data as a server
    def sendData(self, data):
        self.conn.send(str.encode(data))