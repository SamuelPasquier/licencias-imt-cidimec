from django.db import models
import datetime
import os

# Create your models here.


class estudiantes(models.Model):
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    ci = models.IntegerField()


def custom_upload_to(instance, filename):
    fecha_hora_actual = datetime.datetime.now()
    fecha_actual = fecha_hora_actual.date()
    hora_actual = fecha_hora_actual.time()

    _, file_extension = os.path.splitext(filename)

    new_filename = f'{fecha_actual}_{hora_actual}{file_extension}'

    return f'pdfs/{new_filename}'


class permisos(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    )

    CHOICES = (
        ('salud', 'Salud'),
        ('actividad academica', 'Actividad académica'),
        ('actividad deportiva/cultural', 'Actividad deportiva/cultural'),
        ('asunto familiar', 'Asunto familiar'),
        ('otro', 'Otro'),
    )
    materia = models.CharField(max_length=200)
    fecha = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    justificacion = models.FileField(upload_to=custom_upload_to, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True, default=' ')
    justificacion2 = models.FileField(upload_to=custom_upload_to, null=True, blank=True)
    fechaSolicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendiente')
    project = models.ForeignKey(estudiantes, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=30, choices=CHOICES, default='Otro')
    observaciones = models.TextField(null=True, blank=True)
    id_solicitud = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.materia
