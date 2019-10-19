from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=200)
    detalle = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def str(self):
        return self.nombre