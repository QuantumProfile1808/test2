from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, createRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse



class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
#

class getRoomView(APIView):
    serializer_class = RoomSerializer
    lookup_url_kwarg = 'code'


    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code is not None:
            rooms = Room.objects.filter(code=code)
            if rooms.exists():
                data = RoomSerializer(rooms[0]).data
                data['is_host'] = self.request.session.session_key == rooms[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Bad Request': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({"Bad Request": "Code parameter not found in request"}, status=status.HTTP_400_BAD_REQUEST)


class JoinRoom (APIView):

    lookup_url_kwarg = 'code'
    
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        

        code = request.data.get(self.lookup_url_kwarg) # Get the code from the request data

        if code != None:
            room_result = Room.objects.filter(code=code)

            if len(room_result) > 0:
                room = room_result[0]
                self.request.session['room_code'] = code
                return Response({"message": "Room joined successfully"}, status=status.HTTP_200_OK)
            
            self.request.session['room_code'] = room.code
            return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)


class CreateRoomView (APIView):
    serializer_class = createRoomSerializer


    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    



def index(request, *args, **kwargs):
    return JsonResponse({"message": "API index"})
                

    

