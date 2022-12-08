from django.urls import path

from .views import ProjectMetricsViewSet, ReviewViewSet

urlpatterns = [
    path("projects/metrics/", ProjectMetricsViewSet.as_view({"get": "list"}), name="review-list"),
    path("reviews/", ReviewViewSet.as_view({"get": "list"}), name="review-list"),
]
