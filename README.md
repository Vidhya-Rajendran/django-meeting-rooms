# django-meeting-rooms-booking
Manage, arrange meeting room usage via simple app

## Scope 
The application allows users to:
1. Create a meeting (Book a meeting room)
2. A list of Meeting rooms to view the available meeting rooms

## Tech Stack
1. Python
2. Django
3. Django RestFramework

## Installation

1. Cloning repository 
```
git clone https://github.com/Vidhya-Rajendran/django-meeting-rooms.git
```
2. To Creating and activating virtual environment
```
virtualenv envname --python=python3.6

source envname/bin/activate
```
3. Installing project requirements
```
pip install -r requirements.txt
```
4. To run the project
```
python manage.py runserver
```
## Project Description
### Book a Meeting Room
Give the following details to **Book a Meeting Room**
```
Room Name
Employee ID
Start Time
End Time
```
Room Name and Employee ID can be choosen from the following choices. Start time and End Time are date and time for what time user have to book. Once Meeting room is booked. Then the room status will changed as **Occupied**.If that meeting room's end time less than current date & time then room status will changed as **Available**.
### List of available rooms
Meeting rooms will be shown based on available status


