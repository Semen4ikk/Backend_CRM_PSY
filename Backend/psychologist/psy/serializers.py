from rest_framework import serializers
from .models import ClientCard, Exercise, Course, Reception

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class ClientCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCard
        fields = '__all__'

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'
