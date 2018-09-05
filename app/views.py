from engine.control import Http_Response

def world(request):
    a = Http_Response()
    return a.render("templates/success_page.html")

def index(request):
    a = Http_Response()
    return a.render("templates/error_page.html", {"code":404})
