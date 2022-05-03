import random
import string

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from boards.utils import get_ip
from tasks.forms import TaskForm

from .models import Board


def index(request):
    return render(request, "home.html")


def _get_unique_slug():
    # create a random alphabetical string of 9 characters
    chars = [random.choice(string.ascii_letters) for i in range(9)]
    chars.insert(3, "-")
    chars.insert(7, "-")
    slug = "".join(chars).lower()

    if Board.objects.filter(slug=slug).exists():
        return _get_unique_slug()
    return slug


@require_POST
def create_board(request):
    slug = _get_unique_slug()
    ip = get_ip(request)
    board = Board.objects.create(slug=slug, ip=ip)
    return redirect(board.get_absolute_url())


def view_board(request, slug):
    board = get_object_or_404(Board, slug=slug)
    return render(
        request, "view_board.html", {"board": board, "task_form": TaskForm()}
    )
