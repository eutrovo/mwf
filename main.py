import importlib
from engine.server import Server
from engine.control import url_parse
from urls import url_list
from app.views import error_404
from settings import installed_apps

def reload_all(installed_apps):
    for module in installed_apps:
        module_ = importlib.import_module(module)
        importlib.reload(module_)

# DEFINING SERVER SOCKET
sckt = Server(ip='localhost', port=8080)

# SERVER LOOP
while True:
    request = sckt.receive()
    try:
        #parsing_result may be a view function, or 0
        parsing_result = url_parse(request, url_list)
        if parsing_result == 0:
            sckt._send(error_404(request))
        else:
            try:
                sckt._send(parsing_result(request))
            except:
                print(parsing_result(request))
                sckt._send(parsing_result(request).encode('utf-8'))
        sckt.close()
        reload_all(installed_apps)
    except:
        #insert some error massage below and
        #add error types to except args
        sckt.close()
        raise NameError('Something wrong occurred')
