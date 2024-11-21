from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='places/')
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class OneTimePass(models.Model):
    code = models.CharField(max_length=200)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.code

class SubscriptionPass(models.Model):
    code = models.CharField(max_length=200)
    expires = models.DateTimeField()

    def __str__(self):
        return self.code