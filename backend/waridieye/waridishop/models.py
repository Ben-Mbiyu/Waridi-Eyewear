from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/')
    specs = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
