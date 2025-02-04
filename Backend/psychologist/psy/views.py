from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ClientCardSerializer, ReceptionSerializer, CourseSerializer, \
    ExerciseSerializer
from .models import ClientCard, Course, Reception, Exercise


# Create your views here.

class ClientCardViewSet(viewsets.ModelViewSet):
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer

class ReceptionViewSet(viewsets.ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

