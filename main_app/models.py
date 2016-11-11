import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    GENDER_CHOICES = (
        ('Activo','Activo'),
        ('Inactivo','Inactivo'),
    )
    estado = models.CharField(max_length=100,choices=GENDER_CHOICES)
    fechaInactividad = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.nombre

    def clean(self):
        if self.estado =="Inactivo":
            self.fechaInactividad = datetime.date.today()
        else:
             self.fechaInactividad = " "

class Bonificacion(models.Model):
    idEmpleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    BonificacionCuota = models.FloatField()
    fechaBonificacion = models.DateField()

    def __str__(self):
        return str(self.BonificacionCuota)


class Retencion(models.Model):
    idEmpleado = models.ForeignKey(Empleado)
    RetencionCuota = models.FloatField()
    fechaRetencion = models.DateField()

    def __str__(self):
        return str(self.RetencionCuota) + str(self.idEmpleado)

class Igss(models.Model):
    anio = models.IntegerField()
    cuota_igss = models.FloatField()


class SalarioOrdinario(models.Model):
    anio = models.IntegerField()
    cuota_salario = models.FloatField()

class Planilla(models.Model):
    anio = models.IntegerField()
    mes = models.IntegerField()

class PlanillaGenerar(models.Model):
    empleado_planilla = models.CharField(max_length=100)
    apellido_planilla = models.CharField(max_length=100)
    fecha_inicio_planilla = models.CharField(max_length=100)
    igss_anio_planilla  = models.IntegerField()
    igss_cuota  = models.FloatField()
    mes_planilla = models.IntegerField()
    cuota_salario_planilla  = models.FloatField()
    bonificacion_planilla = models.FloatField()
    retencion_planilla = models.FloatField()
    sueldoTotal_planilla  = models.FloatField()
    sueldoLiquido_planilla  = models.FloatField()

    def __str__(self):
        return self.empleado_planilla,self.apellido_planilla,self.fecha_inicio_planilla,self.igss_anio_planilla
