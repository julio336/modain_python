from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Product(models.Model):
    name = models.CharField(("Name of the product"), max_length=255)
    description = models.CharField(("Describe the product"), max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)


class Comment(models.Model):
    comment = models.CharField(("What is your comment?"), max_length=255)
    usuario = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Product, related_name="producto_comentario", on_delete=models.CASCADE)


    def __str__(self):
        return "{}".format(self.comment)

class ImageProduct(models.Model):
    description = models.CharField(("Describe la imagen"), max_length=255)
    producto = models.ForeignKey(Product, related_name="producto_imagen", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="imagenes_producto")

    def __str__(self):
        return "{}".format(self.description)

class ShoppingCart(models.Model):
    producto = models.ForeignKey(Product, related_name="producto_carrito", on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), related_name="carrito_usuario", on_delete=models.CASCADE)
    precio = models.IntegerField()
    direccion = models.CharField(max_length=255)
    datos_payu = models.CharField(max_length=600)
    


    def __str__(self):
        return "{} {}".format(self.usuario, self.producto)