from rest_framework import serializers
from vital_management_system.models import UserRecords, VitalRecords, UserVitalRecords

class UserRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecords
        fields = ['username', 'gender', 'age']

    def create(self, validated_data):
        user = UserRecords.objects.create(**validated_data)
        user.save()
        return user

class VitalRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalRecords
        fields = ['vital_id', 'normal_range', 'critical']
    
    def create(self, validated_data):
        vital_record = VitalRecords.objects.create(**validated_data)
        vital_record.save()
        return vital_record

class UserVitalRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVitalRecords
        fields = ['username', 'vital_id', 'value', 'timestamp']
    
    def create(self, validated_data):
        user_vital_record = UserVitalRecords.objects.create(**validated_data)
        return user_vital_record
    
