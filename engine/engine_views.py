from engine.control import check_slash
from engine.db_mgmt import Mgmt
import json

def user_view(request):
    method = request['method']
    data_json = request['data']
    data = json.loads(data_json)
    mgmt = Mgmt()
    if method == 'GET':
        response = mgmt.read(data['cols'],
                                'users',
                                data['col'],
                                data['filter'])
        content_length = len(response)
        content_type = 'text/plain; charset=utf-8'
        return f'''HTTP/1.1 200 OK \r\n
                   Content-Type: {content_type}\r\n
                   Content-Length: {content_length}\r\n\r\n
                   {response}'''
    elif method == 'POST':
        pass
    elif method == 'DELETE':
        pass
    elif method == 'PUT':
        pass

    #first element is null


def static_view(request):
    ROUTE = request['route']
    ROUTE = check_slash(ROUTE)
    elements = ROUTE.split("/")
    extension = elements[3].split('.')[1]
    content_type = "Content-Type: "
    if extension in ("gif","jpeg","png","svg","bmp","webp"):
        content_type += f"image/{extension}"
    elif extension in ("css"):
        content_type += "text/css"
    elif extension in ("midi","mpeg","webm","ogg","wav"):
        content_type += f"audio/{extension}"
    elif extension in ("webm","ogg"):
        content_type += f"video/{extension}"
    elif extension == "js":
        content_type += "application/javascript"
    try:
        static_file = open(f"static/{elements[2]}/{elements[3]}",'r')
        static_raw = static_file.read()
        static_file.close()
        return f"HTTP/1.1 200 OK\r\n\
                 {content_type}\r\n\
                 Connection: close\r\n\
                 Content-Length: {len(static_raw)}\r\n\r\n\
                 {static_raw}"
    except:
        return "HTTP/1.1 400 Bad Request"
