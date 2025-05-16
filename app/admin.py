from django.contrib import admin
from .models import Token, Utils

# Register your models here.


class TokenAdmin(admin.ModelAdmin):
    list_display = ("token", "created_at", "ip_address")
    search_fields = ("token", "")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)


class UtilsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ai_apikey",
    )
    search_fields = ("name", "ai_apikey")


admin.site.register(Token, TokenAdmin)
admin.site.register(Utils, UtilsAdmin)
