from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import uuid


class Breed(models.Model):  
    title = models.CharField(max_length=50, verbose_name='Порода')

    class Meta:
        verbose_name_plural = 'Породы'
        verbose_name = 'порода'

    def __str__(self):
        return self.title

class Color(models.Model):
    COLORS = [
        (None, 'Выберите окрас'),
        ('Черный', 'Черный'),
        ('Белый', 'Белый'),
        ('Серый', 'Серый'),
        ('Рыжий', 'Рыжий'),
        ('Коричневый', 'Коричневый'),
        ('Пестрый', 'Пестрый'),
        ('Желтый', 'Желтый'),
        ('Зеленый', 'Зеленый'),
        ('Голубой', 'Голубой'),
        ('Бежевый', 'Бежевый'),
    ]

    color = models.CharField(max_length=50, null=True)

class Type(models.Model):
    TYPE_ANIMALS = [
        (None, 'Вид животного'),
        ('Собака', 'Собака'),
        ('Кот', 'Кот'),
        ('Попугай', 'Попугай'),       
    ]

    type_of_animal = models.CharField(max_length=50, null=True)

class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="Регистрационный номер")
    name = models.CharField(max_length=50, verbose_name='Кличка')  
    age = models.SmallIntegerField(null=True, verbose_name='Возраст')
    type_of_animal = models.CharField(max_length=12, null=True, choices=Type.TYPE_ANIMALS, verbose_name='Вид животного')  
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, verbose_name='Порода')
    color = models.CharField(max_length=12, null=True, choices=Color.COLORS, verbose_name='Окрас')
    data = models.DateField(auto_now_add=True, null=True, verbose_name='Дата поступления')
    description = models.TextField(null=True, verbose_name='Описание')
    foto = models.ImageField(upload_to='foto_pet', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name_plural = 'Питомцы'
        verbose_name = 'питомец'
        ordering = [ 'name' ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pets/pet_detail.html', kwargs={'pk': self.pk})
