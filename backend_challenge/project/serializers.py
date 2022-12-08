import statistics

from rest_framework import serializers

from .models import Project, Result, Review, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title")


class ProjectMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "random_average", "random_average_by_task_name")

    random_average = serializers.SerializerMethodField()
    random_average_by_task_name = serializers.SerializerMethodField()

    def get_random_average(self, project):
        return statistics.mean(project.tasks.values_list("results__data__random", flat=True))

    def get_random_average_by_task_name(self, project):
        return {x: None for x, _ in Task.Name.choices}


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "name", "project")

    project = ProjectSerializer()


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ("id", "data", "task")

    task = TaskSerializer()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "decision", "result")

    result = ResultSerializer()
