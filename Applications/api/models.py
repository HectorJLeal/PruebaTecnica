from django.db import models

#Modelo Base

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class Users(Base):
    name = models.CharField('Nombre',max_length=50)
    user = models.CharField('Usuario',max_length=50)
    #Contraseña sin encriptar
    password = models.CharField('Contraseña',max_length=12)

    def __str__(self):
        return self.name

class Bienes(Base):
    articulo = models.CharField('Articulo',max_length=255)
    descripcion = models.CharField('Descripción',max_length=255)
    usuario_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.articulo
