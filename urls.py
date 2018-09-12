import re
from app import views
from engine.control import url
from engine.engine_views import static_view, user_view

# new
url_list = [
    url(r"^/$", views.index),
    url(r"^/static/(\w+)/", static_view),
    url(r"^/users/?$", user_view)
]
