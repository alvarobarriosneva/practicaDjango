from django.db import models


class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    tipo_membresia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateTimeField()

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=50)
    entrenador = models.ForeignKey(
        Entrenador,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre