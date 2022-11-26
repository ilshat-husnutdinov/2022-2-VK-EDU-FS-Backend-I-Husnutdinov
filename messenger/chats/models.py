from django.db import models
from users.models import AppUser


class Chat(models.Model):
    description = models.TextField(
        max_length=200,
        verbose_name='описание',
        blank=True,
        null=True
        )
    title = models.CharField(max_length=50, verbose_name='название', default='')
    is_archive = models.BooleanField(default=False, verbose_name='в архиве')
    creation_time = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    objects = models.Manager()


    class Meta:
        verbose_name        = 'чат'
        verbose_name_plural = 'чаты'
        ordering = ["id"]


    def __str__(self):
        return f"{self.title}"

class ChatMember(models.Model):
    chat = models.ForeignKey(
        Chat,
        verbose_name='чат',
        related_name='chat_chatmember',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    chat_user = models.ForeignKey(
        AppUser,
        verbose_name='пользователь',
        related_name='appuser_chatmember',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    added_at = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)

    class Meta:
        verbose_name        = 'Пользователь чата'
        verbose_name_plural = 'Пользователи чата'
        ordering = ["id"]

    def __str__(self):
        return f"{self.chat_user}, from chat:{self.chat}"


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        related_name='chat_message',
        verbose_name='чат',
        on_delete=models.CASCADE,

    )
    sent_from = models.ForeignKey(
        ChatMember,
        related_name='chatmember_message_sf',
        verbose_name='отправитель',
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=300)
    sending_time = models.DateTimeField(verbose_name='время отправки', auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name='прочитано')

    class Meta:
        verbose_name        = 'сообщение'
        verbose_name_plural = 'сообщения'
# Create your models here.
