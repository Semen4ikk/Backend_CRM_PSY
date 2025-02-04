from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ClientCard, Course, Exercise, Reception


admin.site.register(ClientCard)
admin.site.register(Course)
admin.site.register(Exercise)
admin.site.register(Reception)