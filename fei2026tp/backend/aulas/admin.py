from django.contrib import admin
from .models import carrera, profesor, materia, aula

admin.site.register(carrera)
admin.site.register(profesor)
admin.site.register(materia)
admin.site.register(aula)
