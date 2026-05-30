from django.urls import path
from .views import carreraMixin

urlpatterns = [
    path('carreras/', carreraMixin.as_view(), name='carrera-list-create'),
]