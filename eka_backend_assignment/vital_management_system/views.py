from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from vital_management_system.serializers import UserRecordSerializer, UserVitalRecordsSerializer, VitalRecordsSerializer
from vital_management_system.models import UserRecords, UserVitalRecords
from vital_management_system.utils import get_vitals_aggregate, get_user_vital_percentile

# Create your views here.
class CreateUser(APIView):

    def post(self, request):
        try:
            serializer = UserRecordSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                response = {
                    "status": "success",
                    "message": f"User {user.username} created successfully."
                    }
                return Response(response, status=status.HTTP_201_CREATED)
            
            return Response({"status": "Failed", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)

class GetUserInformation(APIView):

    def get(self, request):

        try:
            username = request.GET.get('username')
            user_records = UserRecords.objects.filter(username=username).all()
            user_records_serializer = UserRecordSerializer(user_records)
            return Response(user_records_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)

class InsertVitalId(APIView):

    def post(self, request):

        try:
            serializer = VitalRecordsSerializer(request.data)
            if serializer.is_valid():
                vital_record = serializer.save()
                response = {
                    "status": "success",
                    "message": f"vital_id {vital_record.vital_id} added successfully"
                    }
                return Response(response, status=status.HTTP_201_CREATED)
            
            return Response({"status": "Failed", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)

class InsertUserVital(APIView):

    def post(self, request):

        try:
            serializer = UserVitalRecordsSerializer(request.data)
            if serializer.is_valid():
                vital_record = serializer.save()
                response = {
                    "status": "success",
                    "message": f"vital_id {vital_record.vital_id} added successfully"
                    }
                return Response(response, status=status.HTTP_201_CREATED)
            return Response({"status": "Failed", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)

class GetUserVitals(APIView):

    def post(self, request):

        try:
            json_data = request.data
            username = json_data["username"]
            period = json_data["period"]

            start_time = period[0]
            end_time = period[1]

            user_vitals = UserVitalRecords.objects.filter(username=username, timestamp__range=(start_time, end_time))
            user_vitals_serializer = UserVitalRecordsSerializer(user_vitals)
            return Response(user_vitals_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)

class UserVitalsAggregate(APIView):

    def post(self, request):

        try:
            json_data = request.data
            username = json_data.get("username")
            vital_ids = json_data.get("vital_ids")
            start_timestamp = json_data.get("start_timestamp")
            end_timestamp = json_data.get("end_timestamp")

            user_vital_aggregates = {}
            for vital_id in vital_ids:
                user_vital_aggregate = get_vitals_aggregate(vital_id, username, start_timestamp, end_timestamp)
                user_vital_aggregates[vital_id] = user_vital_aggregate

            response = {
                    "status": "success",
                    "message": "Aggregate fetched successfully.",
                    "data": {
                        "username": username,
                        "aggregates": user_vital_aggregate,
                        "start_timestamp": start_timestamp,
                        "end_timestamp": end_timestamp
                    }
                }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)

class PopulationInsights(APIView):

    def post(self, request):
        
        try:
            json_data = request.data
            username = json_data.get("username")
            vital_id = json_data.get("vital_id")
            start_timestamp = json_data.get("start_timestamp")
            end_timestamp = json_data.get("end_timestamp")

            user_vital_records = UserVitalRecords.objects.filter(vital_id=vital_id).all()
            target_aggregate, user_vital_aggregates = 0, []
            for user_vital in user_vital_records:
                vital_aggregate = get_vitals_aggregate(vital_id, user_vital.username, start_timestamp, end_timestamp)
                if username == user_vital.username:
                    target_aggregate = vital_aggregate

            percentile = get_user_vital_percentile(target_aggregate, user_vital_aggregates)

            response =   {
                "status": "success",
                "message": "Population insight fetched successfully.",
                "data": {
                    "username": username,
                    "vital_id": vital_id,
                    "start_timestamp": start_timestamp,
                    "end_timestamp": end_timestamp,
                    "insight": f"Your HeartRate is in the {percentile} percentile."  
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserVitals(APIView):

    def post(self, request):

        try:
            json_data = request.data
            username = json_data.get("username")
            vital_id = json_data.get("vital_id")
            timestamp = json_data.get("timestamp")

            UserVitalRecords.objects.filter(username=username, vital_id=vital_id, timestamp=timestamp).delete()

            response = ({
                "status": "success",
                "message": f"Vital {vital_id} deleted for {username}."
            })
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)

class UpdateUserVital(APIView):

    def post(self, request):

        try:
            json_data = request.data
            username = json_data.get("username")
            vital_id = json_data.get("vital_id")
            timestamp = json_data.get("timestamp")
            updated_value = json_data.get("updated_value")

            UserVitalRecords.objects.filter(username=username, vital_id=vital_id, timestamp=timestamp).update(value=updated_value)
            response =  {"status": "success", "message": f"vital {vital_id} updated for {username}"}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "Failed", "message": f"some error occured {e}"}, status=status.HTTP_400_BAD_REQUEST)
