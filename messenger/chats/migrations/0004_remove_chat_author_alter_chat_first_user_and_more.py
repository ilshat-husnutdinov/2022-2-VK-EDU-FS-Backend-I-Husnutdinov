# Generated by Django 4.1.2 on 2022-10-24 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0003_alter_chat_options_remove_chat_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='author',
        ),
        migrations.AlterField(
            model_name='chat',
            name='first_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatuser_chat_fu', to=settings.AUTH_USER_MODEL, verbose_name='первый пользователь'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='second_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatuser_chat_su', to=settings.AUTH_USER_MODEL, verbose_name='второй пользователь'),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_message', to='chats.chat', verbose_name='чат'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatuser_message_sf', to=settings.AUTH_USER_MODEL, verbose_name='отправитель'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatuser_message_st', to=settings.AUTH_USER_MODEL, verbose_name='получатель'),
        ),
    ]