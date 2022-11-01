from django.contrib import admin
from chats.models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
    filter_horizontal = ('users',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat_id','sent_from','sent_to', 'text')

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
# Register your models here.
