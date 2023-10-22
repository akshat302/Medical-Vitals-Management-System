from django.db import models

# Create your models here.
class UserRecords(models.Model):
    username = models.CharField(max_length=64, unique=True)
    gender = models.CharField(max_length=64)
    age = models.IntegerField()
    medical_conditions = models.JSONField(null=True, blank=True)

class VitalRecords(models.Model):

    vital_id = models.CharField(max_length=128, unique=True, primary_key=True)
    normal_range = models.CharField(max_length=32)
    critical = models.CharField(max_length=32)

class UserVitalRecords(models.Model):

    username = models.ForeignKey(UserRecords, on_delete=models.CASCADE, to_field='username')
    vital_id = models.ForeignKey(VitalRecords, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    timestamp = models.DateTimeField()