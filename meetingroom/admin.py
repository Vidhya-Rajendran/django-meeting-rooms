from django.contrib import admin

# Register your models here.
from meetingroom.models import MeetingRoom, Booking, EmployeeDetails

admin.site.register(MeetingRoom)
admin.site.register(Booking)
admin.site.register(EmployeeDetails)