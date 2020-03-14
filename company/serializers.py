import datetime

from django.db.models import Q
from pytz import timezone
from rest_framework import serializers

from meetingroom.models import Booking, MeetingRoom, EmployeeDetails


def get_emp_id():
    return EmployeeDetails.objects.all().values_list('employee_id', flat=True)


class BookingSerializer(serializers.ModelSerializer):
    room_name = serializers.ChoiceField(write_only=True, choices=[])
    rooms_name = serializers.CharField(source='room_id.room_name', default=None, read_only=True)
    employee_name = serializers.CharField(source='emp_id.employee_name', read_only=True, default=None)
    emp_id = serializers.ChoiceField(write_only=True, choices=get_emp_id())

    # def get_rooms_name(self,obj):

    def __init__(self, *args, **kwargs):
        super(BookingSerializer, self).__init__(*args, **kwargs)
        active = Booking.objects.filter(~Q(Q(start_time__gt=datetime.datetime.now()) |
                                           Q(end_time__lt=datetime.datetime.now()))).values_list('room_id_id')

        rooms = list(MeetingRoom.objects.filter(~Q(id__in=active))
                     .values_list('room_name', flat=True))
        self.fields['room_name'].choices = rooms
        Booking.objects.filter(room_id__room_name__in=rooms).update(status='Available')

    class Meta:
        model = Booking
        fields = ("room_name", "employee_name", "emp_id", "start_time", "end_time", "rooms_name")

    def create(self, validated_data):
        print(validated_data)
        validated_data.pop('emp_id', None)
        validated_data.pop('room_name', None)
        print(validated_data, 'after')
        bookings = Booking.objects.create(status='Occupied', **validated_data)
        return bookings

