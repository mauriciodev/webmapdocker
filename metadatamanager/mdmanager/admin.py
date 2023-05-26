from django.contrib import admin
from moderation.admin import ModerationAdmin

# Register your models here.
from mdmanager.models import product

class ProductAdmin(ModerationAdmin):
    admin_integration_enabled = True

#admin.site.register(product)
admin.site.register(product, ProductAdmin)
