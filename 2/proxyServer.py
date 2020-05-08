from socket import *


class ProxyServer:
    def __init__(self):
        self.server_port = 7999 # default port
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        # automatically change the port if binding failed
        while 1:
            try:
                self.server_socket.bind(('0.0.0.0', self.server_port))
                print('Succefully binded the socket to port ' + self.server_port)
                break
            except OSError:
                print('Port ' + self.server_port + 'is being used...')
                self.server_port += 1
