from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from boards.models import Board

from .forms import CategoryForm, SnoozeForm, TaskForm, TaskUpdateForm
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


def snooze_task(request, board_slug, task_id):
    task = get_object_or_404(
        Task, id=task_id, category__board__slug=board_slug
    )
    if request.method == "POST":
        form = SnoozeForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect(task.category.board.get_absolute_url())
    else:
        form = SnoozeForm(instance=task)
    return render(
        request,
        "render_form.html",
        {
            "form": form,
            "title": f"Snooze {task.title}",
            "submit": "Snooze",
        },
    )


@require_POST
def update_task(request, board_slug, task_id):
    task = get_object_or_404(
        Task, id=task_id, category__board__slug=board_slug
    )
    form = TaskUpdateForm(request.POST, instance=task)
    if form.is_valid():
        task.completed_at = (
            timezone.now() if form.cleaned_data.get("is_completed") else None
        )
        task = form.save()
        return JsonResponse({"success": form.cleaned_data})
    else:
        return JsonResponse({"error": form.errors.as_json()}, status=400)


def edit_task(request, board_slug, task_id):
    task = get_object_or_404(
        Task, id=task_id, category__board__slug=board_slug
    )
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(task.category.board.get_absolute_url())
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        "render_form.html",
        {
            "form": form,
            "title": f"Edit {task.title}",
            "submit": "Save",
        },
    )


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
    category.tasks = category.task_set.filter(completed_at=None)
    return render(
        request,
        "parts/category_tasks.html",
        {"form": form, "category": category},
    )


def edit_category(request, board_slug, category_id):
    category = get_object_or_404(
        Category, board__slug=board_slug, id=category_id
    )
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect(category.board.get_absolute_url())
    else:
        form = CategoryForm(instance=category)
    return render(
        request,
        "dblclick_form.html",
        {
            "form": form,
            "submit": "Save",
        },
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
