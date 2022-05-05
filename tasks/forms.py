from django import forms

from .models import Category, Task


class SnoozeForm(forms.ModelForm):
    snoozed_till = forms.DateField(
        required=True, widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Task
        fields = ["snoozed_till"]


class TaskUpdateForm(forms.ModelForm):
    is_completed = forms.BooleanField(required=False)

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "is_completed",
        ]


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
    name = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": "autofocus"})
    )

    class Meta:
        model = Category
        fields = ["name"]
