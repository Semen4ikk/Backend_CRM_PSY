from django.urls import include, path
from rest_framework import routers

from .views import (
    CourseViewSet, ClientCardViewSet, ExerciseViewSet, ReceptionViewSet,

)

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'clientCard', ClientCardViewSet)
router.register(r'exercise', ExerciseViewSet)
router.register(r'reception', ReceptionViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]