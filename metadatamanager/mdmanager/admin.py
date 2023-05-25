from django.contrib import admin
from moderation.admin import ModerationAdmin

# Register your models here.
from mdmanager.models import metadata

class MetadataAdmin(ModerationAdmin):
    admin_integration_enabled = True

#admin.site.register(metadata)
admin.site.register(metadata, MetadataAdmin)
