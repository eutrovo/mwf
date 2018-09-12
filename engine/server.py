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

    def listen_accept(self):
        self.sock.listen(5)
        (client_socket, address) = self.sock.accept()
        print(f'{address} connected')
        return client_socket

    def receive(self, client_socket):
        '''
        Get the request from user and slices it into important chunks
        '''
        return client_socket.recv(8192)

    def send(self, client_socket, msg):
        '''
        sends a response from a view
        '''
        client_socket.send(msg)

    def close(self, client_socket):
        '''
        simply closes the connection
        '''
        client_socket.shutdown(1)
        client_socket.close()
    def handle_client(self,
                        client_socket,
                        url_parse,
                        url_list,
                        error_404):
        http_request = self.receive(client_socket).decode('utf-8')
        #parsing_result may be a view function, or 0
        parsing_result = url_parse(http_request, url_list)
        if parsing_result == 0:
            self.send(client_socket, error_404(parsing_result))
        else:
            try:
                self.send(client_socket, parsing_result["view"](
                parsing_result)
                )
                self.close(client_socket)
            except TypeError:
                self.send(client_socket, parsing_result["view"](
                parsing_result).encode('utf-8')
                )
                self.close(client_socket)
