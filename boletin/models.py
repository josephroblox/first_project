from django.db import models

# Create your models here.
class Registrado(models.Model):
      nombre = models.CharField(max_length=100, blank=False, null=False)
      email = models.EmailField(blank=True, null=True)
      timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)



      def __str__(self): #python 3
          return self.nombre
      
class Calificacion(models.Model):
    alumno = models.ForeignKey(Registrado)
    clase = models.Charfield(max_length=100, blank=False, null=False)
    nota = models.FloatField()