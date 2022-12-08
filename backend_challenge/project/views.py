from rest_framework import viewsets

from .models import Project, Review
from .serializers import ProjectMetricsSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = (
        Review.objects.all()
        .filter(result__data__random__gte=10, result__data__random__lte=990)
        .order_by("result__data__random")
    )


class ProjectMetricsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMetricsSerializer
    queryset = Project.objects.all()
