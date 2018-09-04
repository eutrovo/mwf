from engine.server import Server
from engine.control import url_parse, Http_Response

# TEST ONLY
a = Http_Response(404, "dalld")
print(a._template_render("templates/error_page.html"))


# DEFINING SERVER SOCKET
sckt = Server(ip='localhost', port=8080)

# SERVER LOOP
'''
while True:
    request = sckt.receive()
    print(request)
    #parsing_result may be a view function, or 0
    parsing_result = url_parse(request)
    if parsing_result == 0:
        sckt._send(b"404, page not found")
    else:
        sckt._send(b"Hello world")
    sckt.close()
'''
