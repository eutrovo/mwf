from engine.control import render

def index(request):
    return render("templates/index.html")

def error_404(request):
    return render("templates/error_page.html", {"code":"404"})
