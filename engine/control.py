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

def render(html_file, variables_dict={}):
    html_file = open(html_file,'r')
    html_raw = html_file.read()
    html_file.close()
    match = re.search(r"\{\{(\w+)\}\}", html_raw)
    if match is not None:
        for match_ in match.groups():
            html_raw = re.sub(r"\{\{" + match_ + r"\}\}", f"{variables_dict[match_]}", html_raw)
    return f"HTTP/1.1 200 OK\n\n\
             {html_raw}".encode('utf-8')
