import re
from urls import url_list


def url_parse(request, url_list = url_list):
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
