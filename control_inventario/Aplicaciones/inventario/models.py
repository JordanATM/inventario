from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo}) - Cantidad: {self.cantidad}"