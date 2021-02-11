from django.urls import path
from .view import CourseListView,CourseDetailsView

urlpatterns = [
    path('',CourseListView.as_view()),
    path('<pk>',CourseDetailsView.as_view())
]