import random
import string

from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from boards.utils import get_ip
from tasks.forms import TaskForm
from tasks.models import Category, Task

from .models import Board

BOARD_COOKIE_KEY = "board_slug"


def index(request):
    if request.COOKIES.get(BOARD_COOKIE_KEY) and "home" not in request.GET:
        board = Board.objects.filter(
            slug=request.COOKIES.get("board_slug")
        ).first()
        if board:
            return redirect(board.get_absolute_url())
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


def _get_board(slug, tasks):
    tasks_prefetch = Prefetch(
        "task_set",
        queryset=tasks,
        to_attr="tasks",
    )
    categories = Prefetch(
        "category_set",
        queryset=Category.objects.prefetch_related(tasks_prefetch),
        to_attr="categories",
    )
    board = get_object_or_404(
        Board.objects.prefetch_related(categories),
        slug=slug,
    )
    return board


def _render_board(request, board):
    base_template = (
        "ajax.html"
        if request.headers.get("x-requested-with") == "XMLHttpRequest"
        else "index.html"
    )
    return render(
        request,
        "view_board.html",
        {
            "board": board,
            "task_form": TaskForm(),
            "base_template": base_template,
        },
    )


def view_board(request, slug):
    tasks = Task.objects.filter(completed_at=None)
    board = _get_board(slug, tasks)
    response = _render_board(request, board)

    # update cookie for board-slug
    saved_board_slug = request.COOKIES.get(BOARD_COOKIE_KEY)
    if saved_board_slug != slug:
        response.set_cookie(BOARD_COOKIE_KEY, slug)
    return response


def view_history(request, board_slug):
    tasks = Task.objects.exclude(completed_at=None)
    board = _get_board(board_slug, tasks)

    # show tasks in completed order
    tasks = []
    for category in board.categories:
        tasks += category.tasks
    tasks.sort(key=lambda x: x.completed_at, reverse=True)
    board.categories = [{"name": "History", "tasks": tasks}]
    return _render_board(request, board)


def view_search(request, board_slug):
    tasks = Task.objects.all()
    board = _get_board(board_slug, tasks)

    # filter tasks based on fuzzy search
    q = request.GET.get("q", "")
    tasks = []
    for category in board.categories:
        for task in category.tasks:
            if q in task.title:
                tasks.append(task)

    search_category = {"name": "Search", "tasks": tasks}
    board.categories = [search_category]

    return _render_board(request, board)
