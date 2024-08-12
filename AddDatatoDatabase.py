import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')      # first folder in db

data = {
    "10051":
        {
            "name": "Paula Ayman",
            "major": "Computer",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "V Good",
            "year": 5,
            "last_attendance_time": "2024-08-11 02:07:13"
        },
    "10052":
        {
            "name": "Paula Emad",
            "major": "Communication",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "V Good",
            "year": 1,
            "last_attendance_time": "2024-08-11 02:07:13"
        },
    "10053":
        {
            "name": "Tony Mikhael",
            "major": "Computer",
            "starting_year": 2023,
            "total_attendance": 12,
            "standing": "V Good",
            "year": 1,
            "last_attendance_time": "2024-08-11 02:07:13"
        },
    "10054":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2010,
            "total_attendance": 7,
            "standing": "V Good",
            "year": 2,
            "last_attendance_time": "2024-08-11 02:07:13"
        },
    "10055":
        {
            "name": "Chris Hemsworth",
            "major": "Economy",
            "starting_year": 2017,
            "total_attendance": 8,
            "standing": "Good",
            "year": 2,
            "last_attendance_time": "2024-08-11 02:07:13"
        },
    "10056":
        {
            "name": "Robert Downey",
            "major": "Acting",
            "starting_year": 2008,
            "total_attendance": 7,
            "standing": "Excellent",
            "year": 7,
            "last_attendance_time": "2024-08-11 02:07:13"
        }
}

for key, value in data.items():     # upload the above date (unzip dictionary)
    ref.child(key).set(value)