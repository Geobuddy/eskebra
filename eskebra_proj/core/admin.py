from django.contrib import admin
from .models import Ads, User
# from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Ads)
admin.site.register(User)

# @admin.register(Ads)
# class ViewAdmin(ImportExportModelAdmin):
#     pass