from django.db import models
from django.urls import reverse
# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100,verbose_name='Имя')
    breed = models.CharField(max_length=100, verbose_name='Порода')

    def __str__(self):
        return self.name



class Client(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    last_name = models.CharField(max_length=50,verbose_name='Фамилия')

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'




class Veterinarian(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    # specialty = models.CharField(max_length=100, verbose_name='Специализация')
    choise = (('Терапевт', 'Терапевт'), ('Хирург', 'Хирург'), ('Дерматолог', 'Дерматолог'),
              ('Гастроэнтеролог', 'Гастроэнтеролог'), ('Кардиолог', 'Кардиолог'),('Ратолог', 'Ратолог'))
    specialty = models.CharField(max_length=50, choices=choise, verbose_name='Специализация')
    def __str__(self):
        return self.specialty


class Appointment(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client}'

    def get_absolute_url(self): # Получает URL страницы объекта
        return reverse('animal-detail',args=[self.id, self.animal])
        #return f'kino/{self.id}/{self.title}