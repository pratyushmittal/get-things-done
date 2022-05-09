from django.urls import include, path

from . import views

app_name = "boards"

urlpatterns = [
    path("", views.index, name="home"),
    path("create/", views.create_board, name="create"),
    path("u/<slug:slug>/", views.view_board, name="view"),
    path("u/<slug:board_slug>/history/", views.view_history, name="history"),
    path("u/<slug:board_slug>/search/", views.view_search, name="search"),
    path("u/<slug:board_slug>/", include("tasks.urls", namespace="tasks")),
]
