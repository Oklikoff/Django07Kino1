from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name, self.last_name


class Veterinarian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.specialty


class Appointment(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)

    def __str__(self):
        return self.client