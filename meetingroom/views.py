from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from company.serializers import BookingSerializer
from meetingroom.models import Booking, MeetingRoom


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class AvailableRooms(APIView):

    def get(self, request):
        get_all = MeetingRoom.objects.all().values_list('id', flat=True)
        query_set = MeetingRoom.objects.filter(Q(booking_room__status='Available')).values_list('room_name', flat=True)
        return Response(data=set(query_set), status=status.HTTP_200_OK)

