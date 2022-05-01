from django.urls import include, path

from . import views

app_name = "boards"

urlpatterns = [
    path("", views.index, name="home"),
    path("create/", views.create_board, name="create"),
    path("u/<slug:slug>/", views.view_board, name="view"),
    path("u/<slug:board_slug>/", include("tasks.urls", namespace="tasks")),
]
