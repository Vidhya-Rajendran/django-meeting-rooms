import datetime

from django.db.models import Q
from pytz import timezone
from rest_framework import serializers

from meetingroom.models import Booking, MeetingRoom, EmployeeDetails


def get_emp_id():
    return EmployeeDetails.objects.all().values_list('employee_id', flat=True)

def get_room_id():
    return MeetingRoom.objects.all().values_list('room_name', flat=True)


class BookingSerializer(serializers.ModelSerializer):
    rooms_name = serializers.CharField(source='room.room_name', default=None, read_only=True)
    room_name = serializers.ChoiceField(required=False, choices=[])
    employee_name = serializers.CharField(source='emp.employee_name', read_only=True, default=None)
    employee_id = serializers.ChoiceField(required=False, choices=get_emp_id())

    def __init__(self, *args, **kwargs):
        super(BookingSerializer, self).__init__(*args, **kwargs)
        active = Booking.objects.filter(~Q(Q(start_time__gt=datetime.datetime.now()) |
                                           Q(end_time__lt=datetime.datetime.now()))).values_list('room')
        rooms = list(MeetingRoom.objects.filter(~Q(id__in=active))
                     .values_list('room_name', flat=True))
        self.fields['room_name'].choices = rooms
        Booking.objects.filter(room__room_name__in=rooms).update(status='Available')

    class Meta:
        model = Booking
        fields = ("employee_name", "room_name", "employee_id", "start_time", "end_time", "rooms_name")

    def create(self, validated_data):
        validated_data['room'] = MeetingRoom.objects.get(room_name=validated_data.get('room_name'))
        validated_data['emp'] = EmployeeDetails.objects.get(employee_id=validated_data.get('employee_id'))
        validated_data.pop('room_name', None)
        validated_data.pop('employee_id', None)
        bookings = Booking.objects.create(status='Occupied', **validated_data)
        return bookings

