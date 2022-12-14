# Generated by Django 4.1.4 on 2022-12-07 23:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("data", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("task-name-1", "Task name 1"),
                            ("task-name-2", "Task name 2"),
                            ("task-name-3", "Task name 3"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="tasks", to="project.project"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "decision",
                    models.BooleanField(choices=[("accepted", "Accepted"), ("rejected", "Rejected")], max_length=50),
                ),
                (
                    "result",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="reviews", to="project.result"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="result",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="results", to="project.task"
            ),
        ),
    ]
