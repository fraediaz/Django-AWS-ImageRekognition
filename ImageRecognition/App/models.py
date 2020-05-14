from django.db import models

# Create your models here.


class Consulta(models.Model):
    img         = models.ImageField('', upload_to='busquedas')
    datos       = models.TextField('Datos', blank=True, null=True)
    def __str__(self):
        return str(self.img)
