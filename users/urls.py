from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_all, name="list_all"),
    path("<uuid:id>", views.get_by_id, name="get_by_id"),
    path("create", views.create, name="create"),
]

# types params-> str | int | slug | path
# str -> Matches any non-empty string
# int -> integer
# slug -> ASCII string consisting of lowercase letters, numbers and hyphens (welcome-to-the-1-room)
# uuid -> Unique Identifier (c1d19dbc-9078-4672-9291-864888ea5066)
# path -> Matches any non-empty string, including the path separator /
