from django.db import models

# tabla carrera
class carrera(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.nombre

# tabla profesor
class profesor(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    apellido = models.CharField(max_length=128, null=False, blank=False)
    mostrar = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
# tabla materia
class materia(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    cant_alumnos = models.IntegerField(default=0, null=False)
    
    # fks
    id_carrera = models.ForeignKey(carrera, on_delete=models.CASCADE, db_column='id_carrera')
    id_profesor = models.ForeignKey(profesor, on_delete=models.CASCADE, db_column='id_profesor')

    def __str__(self):
        return self.nombre
    
# tabla aula
class aula(models.Model):
    descripcion = models.CharField(max_length=128, null=False, blank=False)
    ubicacion = models.CharField(max_length=128, null=False, blank=False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion