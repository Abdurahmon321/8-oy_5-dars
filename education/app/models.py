from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    davomiyligi = models.IntegerField()


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    tajriba = models.IntegerField()
    subject = models.ForeignKey(Course, on_delete=models.CASCADE)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    parents_number = models.CharField(max_length=13)
    telegram_link = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
