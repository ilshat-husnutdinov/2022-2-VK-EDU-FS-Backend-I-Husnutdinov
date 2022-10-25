from django.db import models
from django.contrib.auth.models import AbstractUser


class ChatUser(AbstractUser):
    GENDERS = (
        ('m','Мужчина'),
        ('f','Женщина'),
    )

    gender = models.CharField(max_length=1, choices=GENDERS, default='', verbose_name='пол')
    location = models.CharField(max_length=30, blank=True, verbose_name='город')


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ["id"]

# Create your models here.
