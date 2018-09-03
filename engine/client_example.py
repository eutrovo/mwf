from server import Client

sckt = Client(ip='www.facebook.com', port=80)
sckt.send(b'GET / HTTP/1.1\n\
            Host: localhost:8000\n\
            User-Agent: Client Socket (X11; Ubuntu; Linux x86_64; rv:61.0)\
            Accept: text/html,application/xhtml+xml,application/\
            xml;q=0.9,*/*;q=0.8\n\
            Accept-Language: en-US,en;q=0.7,pt-BR;q=0.3\n\
            Accept-Encoding: gzip, deflate\n\
            Connection: keep-alive\n\
            Upgrade-Insecure-Requests: 1\n\
            ')
msg = sckt.receive()
sckt.close()
print(msg)
