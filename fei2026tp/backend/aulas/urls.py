from django.urls import path
from .views import carreraMixin, profesorMixinDetail

urlpatterns = [
    path('carreras/', carreraMixin.as_view(), name='carrera-list-create'),
    path('profesores/<int:pk>/', profesorMixinDetail.as_view(), name='profesor-detail'),
]