from django.contrib import admin
from .models import carrera, profesor, materia, aula, reserva_aula, horario_materia

admin.site.register(carrera)
admin.site.register(profesor)
admin.site.register(materia)
admin.site.register(aula)
admin.site.register(reserva_aula)
admin.site.register(horario_materia)