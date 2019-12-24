from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import models


@admin.register(models.Options)
class OptionsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Pushes)
class PushesAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'sent', 'is_sent')
    readonly_fields = ('is_sent', )

    def has_delete_permission(self, request, obj=False):
        return False


admin.site.site_header = _("Custom site header")
admin.site.site_title = _("Custom site title")
admin.site.index_title = _("Welcome to admin panel")