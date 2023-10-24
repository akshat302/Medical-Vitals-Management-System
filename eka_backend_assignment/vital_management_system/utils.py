from vital_management_system.models import UserVitalRecords
from django.db.models import Avg

def get_vitals_aggregate(vital_id, username, start_time, end_time):

    vital_aggregate = UserVitalRecords.objects.filter(username=username, vital_id=vital_id, timestamp__range=(start_time, end_time)).aggregate(average=Avg('value'))
    return vital_aggregate["average"]

def get_user_vital_percentile(target_aggregate, user_vital_aggregates):
    count = 0
    for vital_aggregate in user_vital_aggregates:
        if vital_aggregate < target_aggregate:
            count += 1
    return (count/len(user_vital_aggregates))*100