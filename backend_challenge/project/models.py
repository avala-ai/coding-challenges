from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)


class Task(models.Model):
    class Name(models.TextChoices):
        TASK_NAME_1 = "task-name-1", "Task name 1"
        TASK_NAME_2 = "task-name-2", "Task name 2"
        TASK_NAME_3 = "task-name-3", "Task name 3"

    name = models.CharField(max_length=100, choices=Name.choices)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="tasks")


class Result(models.Model):
    data = models.JSONField()
    task = models.ForeignKey(Task, on_delete=models.PROTECT, related_name="results")


class Review(models.Model):
    class Decision(models.TextChoices):
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"

    decision = models.BooleanField(max_length=50, choices=Decision.choices)
    result = models.ForeignKey(Result, on_delete=models.PROTECT, related_name="reviews")
