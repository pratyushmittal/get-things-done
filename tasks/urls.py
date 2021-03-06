from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("add-category/", views.add_category, name="add_category"),
    path(
        "<int:category_id>/edit-category/",
        views.edit_category,
        name="edit_category",
    ),
    path("<int:category_id>/add-task/", views.add_task, name="add_task"),
    path(
        "<int:task_id>/update-status/",
        views.update_status,
        name="update_status",
    ),
    path("<int:task_id>/update/", views.update_task, name="update_task"),
    path("<int:task_id>/edit/", views.edit_task, name="edit"),
    path("<int:task_id>/snooze/", views.snooze_task, name="snooze"),
]
