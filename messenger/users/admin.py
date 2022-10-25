from django.contrib import admin
from users.models import ChatUser


class ChatUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','first_name', 'gender')
    list_filter = ('gender',)


admin.site.register(ChatUser, ChatUserAdmin)
# Register your models here.
