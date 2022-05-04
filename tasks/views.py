from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from boards.models import Board

from .forms import CategoryForm, TaskForm
from .models import Category, Task


@require_POST
def update_status(request, board_slug, task_id):
    task = get_object_or_404(
        Task, id=task_id, category__board__slug=board_slug
    )
    is_completed = request.POST.get("completed") == "true"
    task.completed_at = timezone.now() if is_completed else None
    task.save()
    return JsonResponse({"completed": task.completed_at})


def add_task(request, board_slug, category_id):
    category = get_object_or_404(
        Category, board__slug=board_slug, id=category_id
    )
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.category = category
            task.save()
    else:
        form = TaskForm()
    return render(
        request,
        "parts/category_tasks.html",
        {"form": form, "category": category},
    )


def add_category(request, board_slug):
    board = get_object_or_404(Board, slug=board_slug)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
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
