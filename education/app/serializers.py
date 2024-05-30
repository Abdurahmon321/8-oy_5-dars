from rest_framework import serializers
from .models import Course, Teacher, Student


class CourseSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    davomiyligi = serializers.IntegerField()

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance .davomiyligi = validated_data.get("davommiyligi", instance.davomiyligi)


class TeacherSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)
    tajriba = serializers.IntegerField()
    subject = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.status = validated_data.get("status", instance.status)
        instance.tajriba = validated_data.tajriba("tajriba", instance.tajriba)
        instance.subject = validated_data.get("subject", instance.subject)


class StudentSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=13)
    parent_number = serializers.CharField(max_length=13)
    telegram_link = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=255)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.parent_number = validated_data.get("parent_number", instance.parent_number)
        instance.telegram_link = validated_data.get("telegram_link", instance.telegram_link)
        instance.address = validated_data.get("address", instance.address)
        instance.course = validated_data.get("course", instance.course)
        instance.teacher = validated_data.get("teacher", instance.teacher)
        instance.save()
        return instance

