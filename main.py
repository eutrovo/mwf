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
sckt = Server(ip='localhost', port=8081)
# SERVER LOOP
while True:
    client_socket = sckt.listen_accept()
    sckt.handle_client(client_socket,
                        url_parse,
                        url_list,
                        error_404)
    reload_all(installed_apps)
