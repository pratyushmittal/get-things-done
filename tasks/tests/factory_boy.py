import factory

from tasks.models import Category, Task


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "General Tasks"


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = "Publish repo on Github"
    description = "Create new repo on Github"
    category = factory.SubFactory(CategoryFactory)
