from django.db import models
from django.forms import DateTimeField


# Create your models here.

class Exercise(models.Model):
    number = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return {self.number}, {self.doctor} ,{self.description}

class ClientCard(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=11)
    email = models.CharField(max_length=255)
    passport_number = models.IntegerField(max_length=11)
    description = models.TextField()

    def __str__(self):
        return {self.name}, {self.description}

class Reception(models.Model):
    name = models.CharField(max_length=100)
    overpast = models.BooleanField(default=False)
    start_time = DateTimeField()
    end_time = DateTimeField()
    clientId = models.ForeignKey(ClientCard, on_delete=models.CASCADE)
    exirciseId = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return {self.name},{self.start_time} ,{self.end_time}

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    clientId = models.IntegerField()

    def __str__(self):
        return {self.title},{self.description}
