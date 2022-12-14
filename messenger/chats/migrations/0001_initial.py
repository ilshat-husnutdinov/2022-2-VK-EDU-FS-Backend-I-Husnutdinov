# Generated by Django 4.1.2 on 2022-11-10 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='описание')),
                ('title', models.CharField(default='', max_length=50, verbose_name='название')),
                ('is_archive', models.BooleanField(default=False, verbose_name='в архиве')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'чат',
                'verbose_name_plural': 'чаты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ChatMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')),
                ('chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_chatmember', to='chats.chat', verbose_name='чат')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('sending_time', models.DateTimeField(auto_now_add=True, verbose_name='время отправки')),
                ('is_read', models.BooleanField(default=False, verbose_name='прочитано')),
                ('chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_message', to='chats.chat', verbose_name='чат')),
                ('sent_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatmember_message_sf', to='chats.chatmember', verbose_name='отправитель')),
                ('sent_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chatmember_message_st', to='chats.chatmember', verbose_name='получатель')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
    ]
