# Generated by Django 4.0.4 on 2022-05-03 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0002_rename_create_date_board_created_at"),
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="board",
        ),
        migrations.RemoveField(
            model_name="task",
            name="completed",
        ),
        migrations.AddField(
            model_name="task",
            name="completed_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="boards.board",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="task",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="tasks.category",
            ),
        ),
    ]