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
    
# tabla reserva_aula
class reserva_aula(models.Model):
    # fk aula
    id_aula = models.ForeignKey(aula, on_delete=models.CASCADE, db_column='id_aula')
    
    fh_desde = models.DateTimeField(null=False)
    fh_hasta = models.DateTimeField(null=False)
    observacion = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"Reserva Aula {self.id_aula_id} ({self.fh_desde} - {self.fh_hasta})"
    
# tabla horario_materia
class horario_materia(models.Model):
    # fks materia y reserva_aula
    id_materia = models.ForeignKey(materia, on_delete=models.CASCADE, db_column='id_materia')
    id_reserva = models.ForeignKey(reserva_aula, on_delete=models.CASCADE, db_column='id_reserva')
    
    fh_desde = models.DateTimeField(null=False)
    fh_hasta = models.DateTimeField(null=False)

    def __str__(self):
        return f"Horario Materia {self.id_materia_id} - Reserva {self.id_reserva_id}"