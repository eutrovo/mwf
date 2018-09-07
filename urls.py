from app import views

url_list = {
    "/":views.world,
    r"/static/(\w+)/(\w+)":views.static_view,
}
