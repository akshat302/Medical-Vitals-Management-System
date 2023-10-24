# Medical-Vitals-Management-System

### Requirements

- Django==4.0.6
- djangorestframework==3.13.1
- cryptography==41.0.3

### Steps to run

1. clone the github repo - git clone https://github.com/akshat302/Medical-Vitals-Management-System.git
2. cd into the SuperU-Backend folder - cd Medical-Vitals-Management-System/eka_backend_assignment
3. run python manage.py migrate in the terminal.
4. run python manage.py runserver in the terminal to run the server.

### Entities 

1. UserRecords
2. VitaLRecords
3. UserVitalRecords

### Database Models

UserInformation:

	username: username of the user
	gender: gender of the user
	age:  age of the user
	medical_conditions: medical conditions of the user

VitalRecords

  	vital_id: name of vital_id
    normal_range: normal range of the vital 
    critical: critical value of the vital

UserVitalRecords

  	username: ForeignKey to the user
    vital_id: ForeignKey to the vital records 
    value: value of vital for the user
    timestamp: time at which it is recorded
    
### API Details 

CreateUser -

    URL - "create_user/"
    Type - POST
    Request Body - {
                    "username": "alice",
                    "gender": "female",
                    "age": 29
                  }
    Description: 
      1. Allows to create users
    Response -    {
                    "status": "success",
                    "message": "User bob created successfully."
                  }

GetUserInformation - 
    
    URL - "get_user_information/"
    Type - GET
    Request Params - {
                    "username": "bob"
                    }
    Description :
      1. Retrieves the user information

    Response - {
                  "username": "bob",
                  "gender": "male",
                  "age": 28
              }

InsertVitalId - 

    URL - "insert_vital_id/"
    Type - POST
    Request Body - {
                       "vital_id": "heart_rate",
                      "normal_range": "60-100bpm",
                      "critical": ">120bpm" 
                    }
          
    Description :
      1. Allows to insert new vital ids
      
    Response - {
                  "status": "success",
                  "message": "vital_id heart_rate added successfully"
              }
              
InsertUserVital - 

    URL - "insert_user_vital/"
    Type - POST

    
    Request Body - {
                     "username":"alice",
                    "vital_id": "heart_rate",
                    "value": 12,
                    "timestamp": "2023-10-21T15:09:53.000Z"
                    }
                    
    Description : 
      1. helps to insert vital information for the user
      
    Response - {
                "status": "success",
                "message": "vital_id heart_rate added successfully"
                }
              
  GetUserVitals - 

    URL - "get_user_vitals/"
    Type - POST

      Request Body - {
                  "username": "alice",
                  "period":["2023-10-21T15:09:53.000Z", "2023-10-22T15:09:53.000Z"]
                  }
                  
    Description : 
      1. Retrives the vital information for a user between a time period
      
    Response - [
                  {
                      "username": "alice",
                      "vital_id": "heart_rate",
                      "value": 75,
                      "timestamp": "2023-10-21T14:23:56.377000Z"
                  },
                  {
                      "username": "alice",
                      "vital_id": "heart_rate",
                      "value": 80,
                      "timestamp": "2023-10-21T14:24:58.195000Z"
                  },
                  {
                      "username": "alice",
                      "vital_id": "temperature",
                      "value": 98.6,
                      "timestamp": "2023-10-21T14:25:28.990000Z"
                  }
                }

  UserVitalsAggregate - 

    URL - "user_vitals_aggregate/"
    Type - POST

      Request Body - 
                      {
                          "username": "alice",
                          "vital_ids": ["heart_rate", "temperature"],
                          "start_timestamp": "2023-10-20T14:25:28.990000Z",
                          "end_timestamp": "2023-10-22T14:25:28.990000Z"
                      }


    Description : 
      1. Retrieve average values of specific vitals (or all vitals) for a user over a specified period.
      
    Response -{
                  "status": "success",
                  "message": "Aggregate fetched successfully.",
                  "data": {
                      "username": "alice",
                      "aggregates": {
                          "heart_rate": 77.5,
                          "temperature": 98.6
                      },
                      "start_timestamp": "2023-10-21T18:30:00.000Z",
                      "end_timestamp": "2023-10-22T18:30:00.000Z"
                  }
              }
              
PopulationInsight - 
    
    URL - "population_insight/"
    Type - POST

    Request Body - 
                    {
                        "username": "bob",
                        "vital_id": "heart_rate",
                        "start_timestamp": "2023-10-21T18:30:00.000Z",
                        "end_timestamp": "2023-10-22T18:30:00.000Z"
                    }
    Description :
      1. Compare a user's vitals against the population and provide percentile standings.
    
    Response - 
                {
                "status": "success",
                "message": "Population insight fetched successfully.",
                "data": {
                    "username": "bob",
                    "vital_id": "heart_rate",
                    "start_timestamp": "2023-10-23T18:30:00.000Z",
                    "end_timestamp": "2023-10-25T18:30:00.000Z",
                    "insight": "Your HeartRate is in the 33.33333333333333 percentile."
                }
            }

 DeleteUserVital - 
    
    URL - "delete_user_vital/"
    Type - POST

    Request Body - 
                   {
                      "username": "alice",
                      "vital_id": "heart_rate",
                      "timestamp": "2023-10-21T15:04:07.000Z"
                  }
    Description :
      1. Delete a vital record for a user using the vital ID and timestamp.
    
    Response - 
               {
                  "status": "success",
                  "message": "Vital heart_rate deleted for alice."
              }

UpdateUserVital

    URL - "update_user_vital/"
    Type - POST

    Request Body - 
                   {
                      "username": "alice",
                      "vital_id": "heart_rate",
                      "timestamp": "2023-10-21T15:04:07.000Z"
                  }
    Description :
      1. Update a vital record for a user using the vital ID and timestamp.
    
    Response - 
                {
                  "status": "success",
                  "message": "vital heart_rate updated for alice"
              }
 
