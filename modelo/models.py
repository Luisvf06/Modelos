from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    Nombre=models.CharField(max_length=50)
    Correo_electronico=models.CharField(max_length=100,unique=True)
    Contraseña=models.CharField(max_length=20)
    Fecha_registro=models.DateTimeField(default=timezone.now)

class Proyecto(models.Model):
    Nombre=models.CharField(max_length=100)
    Descripción=models.TextField(max_length=2500) 
    Duración_Estimada=models.FloatField()
    Fecha_de_Inicio=models.DateField(default=timezone.now)#valor por defecto
    Fecha_de_Finalización=models.DateField(default=timezone.now)
    colaboradores=models.ManyToManyField(Usuario,related_name='colaborador')#relacion con Usuarios n-n
    creador=models.ForeignKey(Usuario,related_name='creador',on_delete=models.CASCADE)#relacion con usuario 1-n
    
class Tarea(models.Model):
    Título=models.CharField(max_length=100) 
    Descripción=models.TextField()
    Prioridad=models.IntegerField()
    ESTADIOS=[('PE','Pendiente'),('PR','Progreso'),('Co','Completada')]
    Estadio=models.CharField(max_length=2,choices=ESTADIOS)
    Completada=models.BooleanField()
    Fecha_de_Creación=models.DateField(default=timezone.now)
    Hora_de_Vencimiento=models.TimeField(default=timezone.now)
    creador=models.ForeignKey(Usuario,on_delete=models.CASCADE)#foreign key con usuarios 1-n
    usuario_asignado=models.ManyToManyField(Usuario, through='Asignacion_de_tarea',
                                            related_name='encargados')#relacion con usuario a través de Asignacion_de_tarea
    proyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)

class Asignacion_de_tarea(models.Model):#clase intermedia de Usuario y Tarea
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE)
    Observaciones=models.TextField(max_length=2500)
    Fecha_de_Asignación=models.DateTimeField(default=timezone.now)

class Etiqueta(models.Model):
    etiqueta=models.CharField(max_length=30,unique=True)
    tarea=models.ManyToManyField(Tarea)#relacion con tarea n-n
    

class Comentario(models.Model):
    Contenido=models.TextField(max_length=2500)
    Fecha_de_Comentario=models.DateTimeField(default=timezone.now)
    autor=models.ForeignKey(Usuario,on_delete=models.CASCADE)#relacion 1-n con Usuario
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE)#relacion 1-n con tarea
