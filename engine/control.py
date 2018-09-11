import re

def check_slash(i_str):
    if i_str[-1] == '/':
        return i_str[:-1]
    else:
        return i_str

def url(pattern, view):
    return [pattern, view]

def url_parse(http_request, url_list):
    request_elements = http_request.split('\r\n')[0]\
                                   .split(' ')
    data = http_request.split('\r\n\r\n')[1]
    try:
        method = request_elements[0]
        route = request_elements[1]
    except:
        method = "GET"
        route = "/"
    for url in url_list:
        matches = re.search(url[0], route)
        if matches is not None:
            return {"view": url[1],
                    "method": method,
                    "route": route,
                    "data": data}
    return 0

def render(html_file, variables_dict={}):
    html_file = open(html_file,'r')
    html_raw = html_file.read()
    html_file.close()
    match = re.search(r"\{\{(\w+)\}\}", html_raw)
    if match is not None:
        for match_ in match.groups():
            html_raw = re.sub(r"\{\{" + match_ + r"\}\}",
                              f"{variables_dict[match_]}", html_raw)
    return f"HTTP/1.1 200 OK\r\n\
             Content-Type: text/html; charset=utf-8\r\n\
             Connection: close\r\n\
             Content-Length: {len(html_raw)}\r\n\r\n\
             {html_raw}".encode('utf-8')
