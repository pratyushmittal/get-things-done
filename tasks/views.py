from django.shortcuts import get_object_or_404, redirect, render

from boards.models import Board

from .forms import CategoryForm, TaskForm
from .models import Category


def add_task(request, board_slug, category_id):
    category = get_object_or_404(
        Category, board__slug=board_slug, id=category_id
    )
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            task = form.save(commit=False)
            task.category = category
            task.save()
            return redirect(category.board.get_absolute_url())
    else:
        form = TaskForm()
    return render(
        request,
        "render_form.html",
        {
            "form": form,
            "title": "Add Task",
            "submit": "Create Task",
        },
    )


def add_category(request, board_slug):
    board = get_object_or_404(Board, slug=board_slug)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid:
            category = form.save(commit=False)
            category.board = board
            category.save()
            return redirect(category.board.get_absolute_url())
    else:
        form = CategoryForm()
    return render(
        request,
        "render_form.html",
        {
            "form": form,
            "title": "Create new Group",
            "submit": "Add Group",
        },
    )
