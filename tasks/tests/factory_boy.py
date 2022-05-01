import factory

from tasks.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = "Publish repo on Github"
    description = "Create new repo on Github"
    category = "coding"
