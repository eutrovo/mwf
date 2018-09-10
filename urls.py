import re
from app import views
from engine.control import url, static_view

# new
url_list = [
    url(r"^/$", views.world),
    url(r"^/static/(\w+)/", static_view)
]
