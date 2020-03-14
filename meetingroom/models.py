from django.db import models

# Create your models here.


class MeetingRoom(models.Model):
    room_name = models.CharField(max_length=50)
    room_type = models.CharField(max_length=50)


class EmployeeDetails(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=50)
    employee_designation = models.CharField(max_length=50)
    room_usage = models.BooleanField(default=0)


class Booking(models.Model):
    room = models.ForeignKey('MeetingRoom', null=True, on_delete=models.SET_NULL, related_name='booking_room')
    emp = models.ForeignKey('EmployeeDetails', null=True, on_delete=models.SET_NULL, related_name='employee_booking')
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)
    status = models.CharField(max_length=50, default='Available')
