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
        query_set = MeetingRoom.objects.filter(is_available=1).values('room_name', 'room_type')
        return Response(data=list(query_set), status=status.HTTP_200_OK)

