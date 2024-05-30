from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Student, Course, Teacher
from .serializers import TeacherSerializers, StudentSerializers, CourseSerializers
from .permissions import IsOwnerOrReadOnly


class StudentApiView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [IsAuthenticated]


class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.order_by("first_name")
    serializer_class = StudentSerializers
    permission_classes = [IsOwnerOrReadOnly]


class TeacherApiView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [IsAuthenticated]


class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.order_by("full_name")
    serializer_class = TeacherSerializers
    permission_classes = [IsAuthenticated]


class CourseApiView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.order_by("name")
    serializer_class = StudentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
