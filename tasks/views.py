from django.shortcuts import get_object_or_404, redirect, render

from boards.models import Board

from .forms import CategoryForm


def add_task(request):
    return render(request, "add_task.html")


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
    return render(request, "add_category.html", {"form": form})
