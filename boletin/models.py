from django.db import models

# Create your models here.
class Registrado(models.Model):
      nombre = models.CharField(max_length=100, blank=False, null=False)
      email = models.EmailField(blank=True, null=True)
      timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)



      def __str__(self): #python 3
          return self.nombre
 #CASCADE: borra automaticamente todos los registros relacionados
 #PROTECT: evita que se borren si tiene registros relacionados 
 #SET_NULL: coloca en valor nulo todos los valores relacionados     
class Calificacion(models.Model):
    alumno = models.ForeignKey(Registrado,on_delete=models.PROTECT)
    clase = models.CharField(max_length=100, blank=False, null=False)
    nota = models.FloatField()
    