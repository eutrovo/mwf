import re

def url(pattern, view):
    return [pattern, view]


def url_parse(request, url_list):
    for url in url_list:
        matches = re.search(url[0], request['route'])
        if matches is not None:
            return url[1]
    return 0

def static_view(request):
    ROUTE = request['route']
    if ROUTE[-1] == '/':
        ROUTE = ROUTE[:-1]
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
        print(content_type)
        static_file = open(f"static/{elements[2]}/{elements[3]}",'r')
        static_raw = static_file.read()
        static_file.close()
        return f"HTTP/1.1 200 OK\n\
                 {content_type}\n\
                 Content-Length: {len(static_raw)}\n\n\
                 {static_raw}"
    except:
        return "HTTP/1.1 400 Bad Request"

def render(html_file, variables_dict={}):
    html_file = open(html_file,'r')
    html_raw = html_file.read()
    html_file.close()
    match = re.search(r"\{\{(\w+)\}\}", html_raw)
    if match is not None:
        for match_ in match.groups():
            html_raw = re.sub(r"\{\{" + match_ + r"\}\}",
                              f"{variables_dict[match_]}", html_raw)
    return f"HTTP/1.1 200 OK\n\
             Content-Type: text/html; charset=utf-8\n\
             Content-Length: {len(html_raw)}\n\n\
             {html_raw}".encode('utf-8')
