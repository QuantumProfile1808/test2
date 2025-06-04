from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

class createRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('host', 'guest_can_pause', 'votes_to_skip')
        read_only_fields = ('host',) # host is set in the view, so it should not be writable from the API   