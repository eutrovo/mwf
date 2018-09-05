from engine.server import Server
from engine.control import url_parse
from urls import url_list

# DEFINING SERVER SOCKET
sckt = Server(ip='localhost', port=8080)

# SERVER LOOP

while True:
    request = sckt.receive()
    print(request)
    #parsing_result may be a view function, or 0
    parsing_result = url_parse(request, url_list)
    if parsing_result == 0:
        sckt._send("HTTP/1.1 404 Not Found\n\n<html><body><center><h3>Error 404: File not found</h3><p>Try elsewhere</p></center></body></html>".encode('utf-8'))
    else:
        sckt._send(parsing_result(request).encode('utf-8'))
    sckt.close()
