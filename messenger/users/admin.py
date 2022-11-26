from django.contrib import admin
from users.models import AppUser


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','first_name', 'gender')
    list_filter = ('gender',)


admin.site.register(AppUser, AppUserAdmin)
# Register your models here.
