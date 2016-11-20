from abc import ABC, abstractmethod


class SocketAbstract(ABC):

    @abstractmethod
    def closeSocket(self):
        pass


class ClientSocketAbstract(SocketAbstract):

    @abstractmethod
    def startSocket(self):
        pass

    @abstractmethod
    def receiveData(self):
        pass

    @abstractmethod
    def sendData(self, data):
        pass


class ServerSocketAbstract(SocketAbstract):

    @abstractmethod
    def startSocket(self):
        pass

    @abstractmethod
    def receiveData(self):
        pass

    @abstractmethod
    def sendData(self, data):
        pass
