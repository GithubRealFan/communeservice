from django.contrib import admin
from .models import Server, HotKey, ColdKey
# Register your models here.

class ColdKeyAdmin(admin.ModelAdmin):
    list_display = ('walletname', 'ss58')

class HotkeyAdmin(admin.ModelAdmin):
    list_display = ('walletname', 'hotkey')

class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'ip', 'port', 'power')

admin.site.register(HotKey, HotkeyAdmin)
admin.site.register(ColdKey, ColdKeyAdmin)
admin.site.register(Server, ServerAdmin)