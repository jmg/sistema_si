from django.db import models

class Persona(models.Model):

    nombre = models.CharField(max_length=500, blank=True, null=True)
    apellido = models.CharField(max_length=500, blank=True, null=True)
    dni = models.CharField(max_length=500, blank=True, null=True)
    fecha_de_nacimiento = models.DateTimeField(blank=True, null=True)

    zonas = models.ManyToManyField("Zona", blank=True, null=True)
    ubicaciones = models.ManyToManyField("Ubicacion", blank=True, null=True)


class Ubicacion(models.Model):

    calle_1 = models.CharField(max_length=500, blank=True, null=True)
    calle_2 = models.CharField(max_length=500, blank=True, null=True)
    calle_3 = models.CharField(max_length=500, blank=True, null=True)


class Zona(models.Model):

    nombre = models.CharField(max_length=500, blank=True, null=True)


class Tramite(models.Model):

    persona = models.ForeignKey("Persona", blank=True, null=True)
    fecha_de_inicio = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=500, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
