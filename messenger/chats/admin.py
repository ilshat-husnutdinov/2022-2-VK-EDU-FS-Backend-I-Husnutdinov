from django.contrib import admin
from chats.models import Chat, Message, ChatMember

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat_id','sent_from', 'text')


class ChatMemberAdmin(admin.ModelAdmin):
    list_display = ('id','chat','chat_user')


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(ChatMember, ChatMemberAdmin)
# Register your models here.
