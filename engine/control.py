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

class Http_Response:
    def __init__(self):
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

    def _template_render(self, html_file, variables_dict):
        '''
        intend to render html files
        '''
        html_file = open(html_file,'r')
        html_raw = html_file.read()
        html_file.close()
        match = re.search(r"\{\{(\w+)\}\}", html_raw)
        if match is not None:
            for match_ in match.groups():
                html_raw = re.sub(r"\{\{" + match_ + r"\}\}", f"{variables_dict[match_]}", html_raw)
        return html_raw

    def render(self, html_file, variables_dict={}):
        HTML = self._template_render(html_file, variables_dict)
        response_element = f'''HTTP/1.1 200 OK\n\n
                               {HTML}'''
        return response_element
