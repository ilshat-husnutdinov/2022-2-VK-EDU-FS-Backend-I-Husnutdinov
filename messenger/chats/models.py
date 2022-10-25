from django.db import models
from users.models import ChatUser


class Chat(models.Model):
    first_user = models.ForeignKey(
        ChatUser,
        related_name='chatuser_chat_fu',
        on_delete=models.SET_NULL,
        verbose_name='первый пользователь',
        null=True,
        blank=True
    )
    second_user = models.ForeignKey(
        ChatUser,
        related_name='chatuser_chat_su',
        on_delete=models.SET_NULL,
        verbose_name='второй пользователь',
        null=True,
        blank=True
    )
    is_archive      = models.BooleanField(default=False, verbose_name='в архиве')
    creation_time   = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name        = 'чат'
        verbose_name_plural = 'чаты'
        ordering = ["id"]

    def __str__(self):
        return f"between {self.first_user} and {self.second_user}"


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
    text = models.CharField(max_length=300)
    sending_time = models.DateTimeField(verbose_name='время отправки', auto_now_add=True)


    class Meta:
        verbose_name        = 'сообщение'
        verbose_name_plural = 'сообщения'
# Create your models here.
