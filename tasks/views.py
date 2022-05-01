from django.shortcuts import render


def add_task(request):
    return render(request, "add_task.html")
