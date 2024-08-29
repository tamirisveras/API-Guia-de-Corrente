from django.db import models

class Tourist(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='tourist/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Hosting(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='hospedagem/images')
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Gastronomic(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurante/images')
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name