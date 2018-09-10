from engine.control import render

def index(request):
    return render("html/index.html")

def error_404(request):
    return render("html/error_page.html", {"code":"404"})
