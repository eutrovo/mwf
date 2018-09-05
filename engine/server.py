import socket

class Server:
    ''' creates a socket to listen to a port '''

    def __init__(self, **kwargs):
        '''
        kwargs: ip = 'your ip', port: port_number (int)
        '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((kwargs['ip'],kwargs['port']))
        print(f"Running on http://{kwargs['ip']}:{kwargs['port']}/")

    def receive(self):
        '''
        Get the request from user and slices it into important chunks
        '''
        self.sock.listen(5)
        (self._client_socket, address) = self.sock.accept()
        print(f'{address} connected')
        message = self._client_socket.recv(8192)
        message = message.decode('utf-8')
        FIRST_LINE = message.split('\r')[0]
        REQUEST_ELEMENTS = message.split(' ')
        try:
            request = {'method': REQUEST_ELEMENTS[0], 'route': REQUEST_ELEMENTS[1]}
        except:
            request = {'method': "GET", "route": "/"}
        return request

    def _send(self, msg):
        '''
        sends a response from a view
        '''
        self._client_socket.send(msg)

    def close(self):
        '''
        simply closes the connection
        '''
        self._client_socket.close()

class Client:

    def __init__(self, **kwargs):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((kwargs['ip'],kwargs['port']))

    def send(self, msg):
        self.sock.send(msg)

    def receive(self):
        msg = self.sock.recv(8192)
        msg = msg.decode('utf-8')
        return msg

    def close(self):
        self.sock.close()
