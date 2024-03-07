from django.db import models
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=1287)


class Topping(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    name = models.CharField(max_length=100)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    summ = models.FloatField()

    # def AddProduct(self,product):
    #     self._products.append(product)
    #     self._summ = 0
    #     for item in self._products:
    #         self._summ += item.price
    # def GetProducts(self):
    #     return self._products
    #
    # def GetSum(self):
    #     return self._summ

