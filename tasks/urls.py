from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("add-category/", views.add_category, name="add_category"),
    path("add-task/", views.add_task, name="add_task"),
]
