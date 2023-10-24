from django.contrib import admin
from vital_management_system.models import UserRecords, VitalRecords, UserVitalRecords

# Register your models here.
admin.site.register(UserRecords)
admin.site.register(VitalRecords)
admin.site.register(UserVitalRecords)
