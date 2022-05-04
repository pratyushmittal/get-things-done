from django import forms

from .models import Category, Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"x-on:keydown.stop": True})
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"x-on:keydown.stop": True}),
    )

    class Meta:
        model = Task
        fields = ["title", "description"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
