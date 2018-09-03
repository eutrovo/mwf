from engine.server import Server
from engine.control import url_parse

# DEFINING SERVER SOCKET
sckt = Server(ip='localhost', port=8000)

# SERVER LOOP
while True:
    request = sckt.receive()
    print(request)
    #parsing_result may be a view function, or 0
    parsing_result = url_parse(request)
    if parsing_result == 0:
        sckt._send(b"404, page not found")
    else:
        sckt._send(parsing_result(request))
    sckt.close()
