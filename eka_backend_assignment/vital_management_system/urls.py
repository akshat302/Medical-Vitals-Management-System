from django.urls import path
from vital_management_system.views import CreateUser, InsertVitalId, InsertUserVital, GetUserInformation, GetUserVitals, PopulationInsights, UserVitalsAggregate, DeleteUserVitals, UpdateUserVital

urlpatterns = [
    path("create_user/", CreateUser.as_view(), name="create_user"),
    path("get_user_information/", GetUserInformation.as_view(), name="get_user_information"),
    path("insert_vital_id/", InsertVitalId.as_view(), name="insert_vital_id"),
    path("insert_user_vital/", InsertUserVital.as_view(), name="insert_user_vital"),
    path("get_user_vitals/", GetUserVitals.as_view(), name="get_user_vitals"), 
    path("population_insight/", PopulationInsights.as_view(), name="population_insight"),
    path("user_vitals_aggregate/", UserVitalsAggregate.as_view(), name="user_vitals_aggregate"),
    path("delete_user_vital/", DeleteUserVitals.as_view(), name="delete_user_vital"),
    path("update_user_vital", UpdateUserVital.as_view(), name="update_user_vital")
]