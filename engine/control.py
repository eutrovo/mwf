import re
from urls import url_list
import datetime


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

class Http_Response:
    def __init__(self, code, html):
        self.code = code
        self.html = html
        self.CODES = {
            "100":"Continue",
            "101":"Switching Protocol",
            "102":"Processing",
            "200":"OK",
            "201":"Created",
            "202":"Accepted",
            "203":"Non-Authoritative Information",
            "204":"No content",
            "205":"Reset Content",
            "206":"Partial Content",
            "207":"Multi-Status",
            "208":"Multi-Status",
            "226":"IM Used",
            "300":"Multiple Choice",
            "301":"Moved Permanently",
            "302":"Found",
            "303":"See Other",
            "304":"Not Modified",
            "305":"Use Proxy",
            "306":"unused",
            "307":"Temporary Redirect",
            "308":"Permanent Redirect",
            "400":"Bad Request",
            "401":"Unauthorized",
            "402":"Payment Required",
            "403":"Forbidden",
            "404":"Not Found",
            "405":"Method Not Allowed",
            "406":"Not Acceptable",
            "407":"Proxy Authentication Required",
            "408":"Request Timeout",
            "409":"Conflict",
            "410":"Gone",
            "411":"Length Required",
            "412":"Precondition Failed",
            "413":"Payload Too Large",
            "414":"URI Too Long",
            "415":"Unsupported Media Type",
            "416":"Requested Range Not Satisfiable",
            "417":"Expectation Failed",
            "418":"I'm a teapot",
            "421":"Misdirected Request",
            "422":"Unprocessable Entity",
            "423":"Locked",
            "424":"Failed Dependency",
            "426":"Upgrade Required",
            "428":"Precondition Required",
            "429":"Too Many Requests",
            "431":"Request Header Fields Too Large",
            "451":"Unavaible For Legal Reasons",
            "500":"Internal Server Error",
            "501":"Not Implemented",
            "502":"Bad Gateway",
            "503":"Service Unavaible",
            "504":"Gateway Timeout",
            "505":"HTTP Version Not Supported",
            "506":"Variant Also Negotiates",
            "507":"Insufficient Storage",
            "508":"Loop detected",
            "510":"Not Extended",
            "511":"Network Authentication Required",
        }

    def _template_render(self, html_file):
        #TODO
        html_raw = open(html_file,'r').read()
        match = re.search(r"\{\{(\w+)\}\}", html_raw)
        for match_ in match.groups():
            print(match_)
            print(f"{match_})
            html_raw = re.sub(match_, html_raw, f"{match_}")
        return html_raw


    def render(self):
        now = datetime.datetime.now()
        HTML = open(self.html,"r").read()
        response_element = f'''HTTP/1.1 {code} {CODES[code]}\n
                               Content-Type: text/html; charset=utf-8\n
                               Date: {now}\n
                               Connection: close\n
                               Content-Length: {len(HTML)}\n
                               \n
                               {HTML}'''
        return response_element



'''HTTP/1.1 400 Bad Request
Content-Type: text/html; charset=utf-8
Date: Mon, 03 Sep 2018 19:12:38 GMT
Connection: close
Content-Length: 2959

<!DOCTYPE html>
'''
