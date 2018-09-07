from engine.control import render

def world(request):
    return render("templates/success_page.html")

def error_404(request):
    return render("templates/error_page.html", {"code":"404"})
