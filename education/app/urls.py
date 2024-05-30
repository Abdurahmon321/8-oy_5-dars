from django.urls import path
from .import views

urlpatterns = [
    path("", views.StudentApiView.as_view(), name="students"),
    path("student/<int:pk>", views.StudentDetailView.as_view()),
    path("teacher/", views.TeacherApiView.as_view(), name="teacher"),
    path("teacher/<int:pk>", views.TeacherDetailView.as_view()),
    path("courses/", views.CourseApiView.as_view(), name="courses"),
    path("courses/<int:pk>", views.CourseDetailView.as_view(), name="courses"),
]