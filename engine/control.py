import re

def url_parse(request, url_list):
    ROUTE = request['route']
    if len(ROUTE) > 1:
        PARSED_ROUTE = re.search(rf'^{ROUTE}/?$',ROUTE)
        STR_ROUTE = PARSED_ROUTE.group(0)
        if PARSED_ROUTE and STR_ROUTE[-1] == "/":
            STR_ROUTE = STR_ROUTE[:-1]
        ROUTE = STR_ROUTE
    for k,v in url_list.items():
        if k == ROUTE:
            return v
    return 0

def static_view(request):
    ROUTE = request['route']
    if ROUTE[-1] == '/':
        ROUTE = ROUTE[:-1]
    elements = ROUTE.split("/")
    app = elements[1]
    resource = elements[2]
    extension = elements[2].split('.')[1]
    content_type = "Content-Type: "
    if extension in ("gif","jpeg","png","svg","bmp","webp"):
        content_type += f"image/{extension}"
    elif extension in ("css"):
        content_type += f"text/css"
    elif extension in ("midi","mpeg","webm","ogg","wav"):
        content_type += f"audio/{extension}"
    elif extension in ("webm","ogg"):
        content_type += f"video/{extension}"
    elif extension == "js":
        content_type += f"application/javascript"
    try:
        static_file = open(f"{elements[1]}/{elements[2]}",'r')
        static_raw = static_file.read()
        static_file.close()
    return f'''HTTP/1.1 200 OK\n
               {content_type}\n
               Content-Length: {len(static_raw)}\n\n
               {static_raw}'''

def render(html_file, variables_dict={}):
    html_file = open(html_file,'r')
    html_raw = html_file.read()
    html_file.close()
    match = re.search(r"\{\{(\w+)\}\}", html_raw)
    if match is not None:
        for match_ in match.groups():
            html_raw = re.sub(r"\{\{" + match_ + r"\}\}", f"{variables_dict[match_]}", html_raw)
    return f"HTTP/1.1 200 OK\n\
             Content-Type: text/html; charset=utf-8\n\
             Content-Length: {len(html_raw)}\n\n\
             {html_raw}".encode('utf-8')
