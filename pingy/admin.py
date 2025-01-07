from django.contrib import admin
from .models import Website


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('address', 'status', 'last_checked', 'owner')
    list_filter = ('status', 'owner')
    search_fields = ('address',)


admin.site.register(Website, WebsiteAdmin)
