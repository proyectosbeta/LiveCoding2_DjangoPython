from django.db import models

# Agregamos la clase Mascota con sus propiedades
class Mascota(models.Model):   # => Emula una Tabla de BD
    SEXO_OPCIONES = [('M','Macho'),('H','Hembra')]
    nombre=models.CharField(max_length=100) #=> Emulan las columnas de una tabla
    doctor=models.CharField(max_length=100)
    especie=models.CharField(max_length=30)
    raza=models.CharField(max_length=30, blank=True)
    descripcion=models.TextField()
    sexo=models.CharField(max_length=1, choices=SEXO_OPCIONES, blank=True)
    fecha=models.DateTimeField()
    edad=models.IntegerField(null=True)

    # Emular la relacion 1:1
    vacunas = models.ManyToManyField('Vacuna', blank=True)

# Agregamos la clase Vacuna con su propiedad y la sobreescritura del método __str__
class Vacuna(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre