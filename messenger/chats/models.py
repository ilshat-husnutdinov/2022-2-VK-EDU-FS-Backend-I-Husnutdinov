from django.db import models
from users.models import ChatUser


class Chat(models.Model):
    users = models.ManyToManyField(
        ChatUser,
        related_name='chatuser_chat',
        verbose_name='пользователи',
    )
    description = models.TextField(
        max_length=200,
        verbose_name='описание',
        blank=True,
        null=True
        )
    title           = models.CharField(max_length=50, verbose_name='название', default='')
    is_archive      = models.BooleanField(default=False, verbose_name='в архиве')
    creation_time   = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    objects = models.Manager()


    class Meta:
        verbose_name        = 'чат'
        verbose_name_plural = 'чаты'
        ordering = ["id"]


    def __str__(self):
        return f"{self.title}"


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        related_name='chat_message',
        verbose_name='чат',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    sent_from = models.ForeignKey(
        ChatUser,
        related_name='chatuser_message_sf',
        verbose_name='отправитель',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sent_to = models.ForeignKey(
        ChatUser,
        related_name='chatuser_message_st',
        verbose_name='получатель',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    text         = models.CharField(max_length=300)
    sending_time = models.DateTimeField(verbose_name='время отправки', auto_now_add=True)
    is_read      = models.BooleanField(default=False, verbose_name='прочитано')

    class Meta:
        verbose_name        = 'сообщение'
        verbose_name_plural = 'сообщения'
# Create your models here.
