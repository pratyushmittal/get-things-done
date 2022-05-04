import random
import string

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from boards.utils import get_ip
from tasks.forms import TaskForm

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


def view_board(request, slug):
    board = get_object_or_404(Board, slug=slug)

    response = render(
        request, "view_board.html", {"board": board, "task_form": TaskForm()}
    )

    # update cookie for board-slug
    saved_board_slug = request.COOKIES.get(BOARD_COOKIE_KEY)
    if saved_board_slug != slug:
        response.set_cookie(BOARD_COOKIE_KEY, slug)
    return response
