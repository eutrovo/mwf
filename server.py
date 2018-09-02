import socket

class Server:
    ''' creates a socket to listen to a port '''

    def __init__(self, **kwargs):
        '''
        kwargs: ip = 'your ip', port: port_number (int)
        '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((kwargs['ip'],kwargs['port']))
        print('Running on http://localhost:8000/')

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
        request = {'method': REQUEST_ELEMENTS[0], 'route': REQUEST_ELEMENTS[1], 'ip': address[0]}
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

if __name__=='__main__':
    sckt = Server(ip='localhost', port=8000)
    while True:
        result = sckt.receive()
        print(result)
        sckt._send(b'hello world')
        sckt.close()
