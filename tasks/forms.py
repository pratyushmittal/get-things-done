from django import forms

from .models import Category, Task


class TaskForm(forms.ModelForm):
    description = forms.CharField(required=False)

    class Meta:
        model = Task
        fields = ["title", "description"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
