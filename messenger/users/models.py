from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    GENDERS = (
        ('m','Мужчина'),
        ('f','Женщина'),
    )

    gender = models.CharField(max_length=1, choices=GENDERS, default='', verbose_name='пол')
    location = models.CharField(max_length=30, blank=True, verbose_name='город')

    def gen_info(self):
        return {
            'id':self.pk,
            'username':self.username,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'is_active':self.is_active,
            'gender':self.gender,
        }

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ["id"]


# Create your models here.
